import tkinter as tk
import os
import threading
import re
import subprocess
import time
import pyperclip
import psutil
from collections import deque
from pynput import mouse
import win32com.client
import ctypes
from ctypes import wintypes
from fuzzywuzzy import fuzz
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import socket

# --- Configuration ---
HOT_CORNER_SENSITIVITY = 5
SEARCH_DIRECTORIES = [os.path.join(os.environ['APPDATA'], 'Microsoft\\Windows\\Start Menu\\Programs'), os.path.expanduser('~\\Documents'), os.path.expanduser('~\\Desktop')]
WATCHED_DIRECTORIES = [os.path.expanduser('~\\Documents'), os.path.expanduser('~\\Desktop')]
PINNED_ITEMS = [{"name": "File Explorer", "path": "explorer.exe"}, {"name": "Documents", "path": os.path.expanduser('~\\Documents')}, {"name": "Downloads", "path": os.path.expanduser('~\\Downloads')}, {"name": "Notepad", "path": "C:\\Windows\\System32\\notepad.exe"}]
SYSTEM_COMMANDS = {"shutdown": {"command": "shutdown /s /t 1", "label": "Off"}, "restart": {"command": "shutdown /r /t 1", "label": "Restart"}, "lock": {"command": "rundll32.exe user32.dll,LockWorkStation", "label": "Lock"}}
WEB_PREFIXES = {"g ": "https://www.google.com/search?q=", "yt ": "https://www.youtube.com/results?search_query=", "gh ": "https://github.com/search?q=", "ddg ": "https://duckduckgo.com/?q=", "b ": "https://www.bing.com/search?q="}

# --- Windows API Definitions ---
class AccentPolicy(ctypes.Structure): _fields_ = [("AccentState", ctypes.c_uint), ("AccentFlags", ctypes.c_uint), ("GradientColor", ctypes.c_uint), ("AnimationId", ctypes.c_uint)]
class WindowCompositionAttributeData(ctypes.Structure): _fields_ = [("Attribute", ctypes.c_int), ("Data", ctypes.POINTER(AccentPolicy)), ("SizeOfData", ctypes.c_size_t)]

# --- Background Services ---
class FileIndexEventHandler(FileSystemEventHandler):
    def __init__(self, indexer): self.indexer = indexer
    def on_any_event(self, event): self.indexer.needs_reindex = True

class BackgroundServices:
    def __init__(self):
        self.app_items = []; self.file_items = []; self.needs_reindex = True; self.observer = Observer()
        self.clipboard_history = deque(maxlen=20); self.last_clipboard_content = ""
        self.start_all_services()
    def index_files(self):
        print("Starting file index..."); temp_apps, temp_files = [], []
        for directory in SEARCH_DIRECTORIES:
            for root_dir, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root_dir, file)
                    # --- FIX: Use the full filename without extension as the name ---
                    name = os.path.splitext(file)[0]
                    ext = os.path.splitext(file)[1]
                    item = {"name": name, "path": file_path}
                    if ext.lower() in ['.lnk', '.exe']: item["type"] = "Application"; temp_apps.append(item)
                    else: item["type"] = "File"; temp_files.append(item)
        self.app_items, self.file_items = temp_apps, temp_files; self.needs_reindex = False
        print(f"Indexing complete. Found {len(self.app_items)} apps and {len(self.file_items)} files.")
    def start_reindex_thread(self): threading.Thread(target=self.index_files, daemon=True).start()
    def start_watching(self):
        event_handler = FileIndexEventHandler(self)
        for path in WATCHED_DIRECTORIES:
            if os.path.exists(path): self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()
    def monitor_clipboard(self):
        while True:
            try:
                current_content = pyperclip.paste()
                if current_content and current_content != self.last_clipboard_content:
                    self.last_clipboard_content = current_content; self.clipboard_history.appendleft(current_content)
            except pyperclip.PyperclipException: pass
            time.sleep(1)
    def start_all_services(self): self.start_watching(); self.start_reindex_thread(); threading.Thread(target=self.monitor_clipboard, daemon=True).start()

# --- Main Application ---
class FluentHubApp:
    def __init__(self, root, services):
        self.root = root; self.services = services
        self.FONT_BOLD = ('Segoe UI', 11, 'bold'); self.FONT_NORMAL = ('Segoe UI', 10); self.FONT_SMALL = ('Segoe UI', 9)
        self.COLOR_TEXT = "#fafafa"; self.COLOR_SUBTEXT = "#a0a0a0"; self.COLOR_SELECTION = "#0078d4"
        self.COLOR_FROSTED_BG = "#282828"; self.COLOR_FROSTED_HOVER = "#404040"; self.COLOR_HANDLE = "#333333"
        self.is_window_visible = False; self._drag_start_x = 0; self._drag_start_y = 0; self.selected_index = -1
        self.in_action_menu = False; self.action_target_item = None; self.selected_action_index = 0
        
        self.shadow = tk.Toplevel(root); self.shadow.withdraw(); self.shadow.overrideredirect(True); self.shadow.attributes("-alpha", 0.3)
        tk.Label(self.shadow, bg="black", fg="white").pack(expand=True, fill='both')
        self.root.withdraw(); self.root.attributes("-topmost", True); self.root.overrideredirect(True)
        self.setup_ui(); self.apply_glass_effect(); self.setup_bindings()

    def apply_glass_effect(self):
        self.root.update(); self.shadow.update()
        hwnd = ctypes.windll.user32.GetParent(self.root.winfo_id()); shadow_hwnd = ctypes.windll.user32.GetParent(self.shadow.winfo_id())
        try:
            DWMWA_WINDOW_CORNER_PREFERENCE = 33; DWMWCP_ROUND = 2
            for handle in [hwnd, shadow_hwnd]: ctypes.windll.dwmapi.DwmSetWindowAttribute(handle, DWMWA_WINDOW_CORNER_PREFERENCE, ctypes.byref(ctypes.c_int(DWMWCP_ROUND)), ctypes.sizeof(ctypes.c_int))
        except: pass
        try:
            DWMWA_SYSTEMBACKDROP_TYPE = 38; DWMSBT_ACRYLIC_BEHINDWINDOW = 3
            ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_SYSTEMBACKDROP_TYPE, ctypes.byref(ctypes.c_int(DWMSBT_ACRYLIC_BEHINDWINDOW)), ctypes.sizeof(ctypes.c_int))
        except:
            ACCENT_ENABLE_ACRYLICBLURBEHIND = 4; accent = AccentPolicy(ACCENT_ENABLE_ACRYLICBLURBEHIND, 2, 0xDD101010, 0)
            data = WindowCompositionAttributeData(19, ctypes.pointer(accent), ctypes.sizeof(accent))
            ctypes.windll.user32.SetWindowCompositionAttribute(hwnd, ctypes.byref(data))
        self.root.config(bg='black'); self.root.attributes("-transparentcolor", "black")

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg="black"); main_frame.pack(fill=tk.BOTH, expand=True)
        sidebar_container = tk.Frame(main_frame, bg="black", width=240); sidebar_container.pack(side=tk.LEFT, fill=tk.Y, padx=(15, 0), pady=15); sidebar_container.pack_propagate(False)
        separator = tk.Frame(main_frame, bg=self.COLOR_FROSTED_BG, width=1); separator.pack(side=tk.LEFT, fill=tk.Y, pady=15)
        content_frame = tk.Frame(main_frame, bg="black"); content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=15, pady=15)
        
        title_bar = tk.Frame(content_frame, bg=self.COLOR_HANDLE, height=30); title_bar.pack(fill=tk.X, side=tk.TOP)
        drag_label = tk.Label(title_bar, text=" ● ● ● ", font=self.FONT_BOLD, bg=self.COLOR_HANDLE, fg=self.COLOR_SUBTEXT); drag_label.pack(side=tk.LEFT, padx=10)
        close_button_style = {'font': ('Segoe UI Symbol', 10), 'bg': self.COLOR_HANDLE, 'fg': self.COLOR_SUBTEXT, 'activebackground': self.COLOR_FROSTED_HOVER, 'activeforeground': self.COLOR_TEXT, 'relief': 'flat', 'borderwidth': 0}
        close_button = tk.Button(title_bar, text="✕", **close_button_style, command=self.hide_window); close_button.pack(side=tk.RIGHT, padx=5)
        self.setup_drag(title_bar); self.setup_drag(drag_label)
        
        canvas = tk.Canvas(sidebar_container, bg="black", highlightthickness=0)
        self.scrollable_frame = tk.Frame(canvas, bg="black")
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw"); canvas.pack(side="left", fill="both", expand=True)
        button_style = {'font': self.FONT_BOLD, 'bg': self.COLOR_FROSTED_BG, 'fg': self.COLOR_TEXT, 'activebackground': self.COLOR_FROSTED_HOVER, 'activeforeground': self.COLOR_TEXT, 'relief': 'flat', 'borderwidth': 0, 'anchor': 'w', 'justify': 'left'}
        for item in PINNED_ITEMS:
            btn = tk.Button(self.scrollable_frame, text=item['name'], **button_style, command=lambda p=item['path']: self.execute_item({"path": p, "type": "PINNED"}))
            btn.pack(fill=tk.X, padx=10, pady=5, ipady=8)

        entry_container = tk.Frame(content_frame, bg=self.COLOR_FROSTED_BG, highlightbackground=self.COLOR_HANDLE, highlightthickness=1); entry_container.pack(fill=tk.X, ipady=1, padx=10, pady=(10, 5))
        self.placeholder_texts = ["Search apps first, then files...", "Try 'clip', 'kill', or 'sys'...", "Press Tab on a file for actions..."]; self.placeholder_index = 0
        self.entry_var = tk.StringVar(value=""); self.entry = tk.Entry(entry_container, textvariable=self.entry_var, font=('Segoe UI Semibold', 20), background=self.COLOR_FROSTED_BG, fg=self.COLOR_TEXT, insertbackground=self.COLOR_TEXT, borderwidth=0, highlightthickness=0)
        self.entry.pack(fill=tk.X, ipady=10, padx=5, pady=5)
        self.placeholder_label = tk.Label(entry_container, text=self.placeholder_texts[0], font=('Segoe UI Semibold', 20), bg=self.COLOR_FROSTED_BG, fg=self.COLOR_SUBTEXT)
        self.placeholder_label.place(x=5, y=5, anchor='nw'); self.placeholder_label.bind("<Button-1>", lambda e: self.entry.focus_set())
        
        self.results_frame = tk.Frame(content_frame, bg=self.COLOR_FROSTED_BG); self.results_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        bottom_bar_frame = tk.Frame(content_frame, bg="black"); bottom_bar_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=(0, 5))
        sys_button_style = {'font': ('Segoe UI', 10, 'bold'), 'bg': self.COLOR_FROSTED_BG, 'fg': self.COLOR_TEXT, 'activebackground': self.COLOR_FROSTED_HOVER, 'activeforeground': self.COLOR_TEXT, 'relief': 'flat', 'borderwidth': 0}
        for data in SYSTEM_COMMANDS.values():
            btn = tk.Button(bottom_bar_frame, text=data['label'], **sys_button_style, command=lambda c=data['command']: self.execute_item({"path": c, "type": "System Command"}))
            btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5, ipady=8)

    def setup_drag(self, widget):
        widget.bind("<ButtonPress-1>", self.on_drag_start); widget.bind("<B1-Motion>", self.on_drag_motion)
    def on_drag_start(self, event): self._drag_start_x = event.x; self._drag_start_y = event.y
    def on_drag_motion(self, event):
        x = self.root.winfo_x() + event.x - self._drag_start_x; y = self.root.winfo_y() + event.y - self._drag_start_y
        self.root.geometry(f"+{x}+{y}"); self.shadow.geometry(f"+{x+5}+{y+5}")

    def setup_bindings(self):
        self.entry.bind('<KeyRelease>', self.on_key_release)
        self.root.bind('<Escape>', self.on_escape); self.root.bind('<Up>', self.select_previous); self.root.bind('<Down>', self.select_next); self.root.bind('<Return>', self.on_enter); self.root.bind('<Tab>', self.on_tab)

    def check_focus(self):
        if self.is_window_visible:
            if self.root.focus_get() is None: self.hide_window()
            else: self.root.after(250, self.check_focus)

    def perform_search(self, query):
        if not query: return []
        results, app_results, file_results = [], [], []
        if query == 'clip': results.extend([{"name": v.strip()[:100] + ('...' if len(v.strip()) > 100 else ''), "path": v, "type": "Clipboard History", "score": 102} for v in self.services.clipboard_history])
        elif query == 'sys': results.extend(self.get_system_info())
        elif query.startswith('kill '):
            proc_query = query.split(' ', 1)[1].lower()
            results.extend([{"name": p.info['name'], "path": f"PID: {p.info['pid']}", "type": "Running Process", "score": 101, "exec_path": p.info['pid']} for p in psutil.process_iter(['pid', 'name']) if proc_query in p.info['name'].lower()])
        for prefix, url in WEB_PREFIXES.items():
            if query.startswith(prefix): results.append({"name": f"Search for: {query.split(prefix, 1)[1]}", "path": f"{url}{query.split(prefix, 1)[1]}", "type": "Web Search", "score": 100})
        if re.match(r'^[\d\s()+\-*/.]+$', query) and len(query) > 1:
            try: results.append({"name": f"= {eval(query)}", "path": "Calculator Result", "type": "Calculation", "score": 100, "exec_path": str(eval(query))})
            except: pass
        app_results = [{**item, "score": fuzz.partial_ratio(query.lower(), item['name'].lower())} for item in self.services.app_items if fuzz.partial_ratio(query.lower(), item['name'].lower()) > 75]
        file_results = [{**item, "score": fuzz.partial_ratio(query.lower(), item['name'].lower())} for item in self.services.file_items if fuzz.partial_ratio(query.lower(), item['name'].lower()) > 75]
        final_results = results + sorted(app_results, key=lambda x: x['score'], reverse=True) + sorted(file_results, key=lambda x: x['score'], reverse=True)
        return final_results[:7]

    def update_ui(self):
        for widget in self.results_frame.winfo_children(): widget.destroy()
        display_list = []
        if self.in_action_menu:
            display_list = [{"name": "Open", "type": "Action"}, {"name": "Open Containing Folder", "type": "Action"}, {"name": "Copy Path to Clipboard", "type": "Action"}]
            current_selection = self.selected_action_index
        elif self.search_results:
            display_list = self.search_results; current_selection = self.selected_index
        
        if display_list:
            for i, item in enumerate(display_list):
                bg = self.COLOR_SELECTION if i == current_selection else self.COLOR_FROSTED_BG
                result_frame = tk.Frame(self.results_frame, bg=bg); result_frame.pack(fill=tk.X, padx=5, pady=2)
                icon_text = {"Application": "🚀", "File": "📄", "Clipboard History": "📋", "Running Process": "⚙️", "System Info": "🖥️", "Action": "▶"}.get(item['type'], "🌐")
                icon_label = tk.Label(result_frame, text=icon_text, font=self.FONT_BOLD, bg=bg, fg=self.COLOR_TEXT); icon_label.pack(side=tk.LEFT, padx=(10, 5), pady=5)
                text_frame = tk.Frame(result_frame, bg=bg); text_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
                title_label = tk.Label(text_frame, text=item['name'], font=self.FONT_BOLD, bg=bg, fg=self.COLOR_TEXT, anchor='w'); title_label.pack(fill=tk.X)
                if not self.in_action_menu:
                    subtitle_text = item['type'] if item['type'] not in ["Application", "File"] else f"...\\{os.path.basename(os.path.dirname(item['path']))}"
                    subtitle_label = tk.Label(text_frame, text=subtitle_text, font=self.FONT_SMALL, bg=bg, fg=self.COLOR_SUBTEXT, anchor='w'); subtitle_label.pack(fill=tk.X)
                # --- THE CRASH FIX IS HERE ---
                # We bind to the frame, which always exists, not its children.
                result_frame.bind("<Button-1>", lambda e, item=item, index=i: self.on_item_click(item, index))
                for child in result_frame.winfo_children():
                    child.bind("<Button-1>", lambda e, item=item, index=i: self.on_item_click(item, index))
        else:
            tk.Label(self.results_frame, text="Ready to search...", font=self.FONT_BOLD, bg=self.COLOR_FROSTED_BG, fg=self.COLOR_SUBTEXT).pack(expand=True)

    def on_item_click(self, item, index):
        if self.in_action_menu: self.selected_action_index = index; self.on_enter()
        else: self.selected_index = index; self.on_enter()

    def on_key_release(self, event):
        if event.keysym in ("Up", "Down", "Return", "Escape", "Tab"): return
        self.in_action_menu = False
        if self.entry_var.get(): self.placeholder_label.place_forget()
        else: self.placeholder_label.place(x=5, y=5, anchor='nw')
        self.search_results = self.perform_search(self.entry_var.get().strip()); self.selected_index = 0 if self.search_results else -1; self.update_ui()

    def select_next(self, event=None):
        if self.in_action_menu:
            if self.selected_action_index < 2: self.selected_action_index += 1
        elif self.selected_index < len(self.search_results) - 1: self.selected_index += 1
        self.update_ui()
    def select_previous(self, event=None):
        if self.in_action_menu:
            if self.selected_action_index > 0: self.selected_action_index -= 1
        elif self.selected_index > 0: self.selected_index -= 1
        self.update_ui()
    
    def on_escape(self, event=None):
        if self.in_action_menu: self.in_action_menu = False; self.update_ui()
        else: self.hide_window()

    def on_tab(self, event=None):
        if not self.in_action_menu and self.search_results and 0 <= self.selected_index < len(self.search_results):
            selected_item = self.search_results[self.selected_index]
            if selected_item['type'] in ["Application", "File"]:
                self.in_action_menu = True; self.action_target_item = selected_item; self.selected_action_index = 0; self.update_ui()
        return "break"

    def on_enter(self, event=None):
        if self.in_action_menu:
            actions = ["Open", "Open Folder", "Copy Path"]; self.execute_action(self.action_target_item, actions[self.selected_action_index])
        elif 0 <= self.selected_index < len(self.search_results): self.execute_item(self.search_results[self.selected_index])

    def execute_action(self, item, action):
        self.hide_window(); path = item['path']
        try:
            if action == "Open": os.startfile(path)
            elif action == "Open Folder": os.startfile(os.path.dirname(path))
            elif action == "Copy Path": pyperclip.copy(path)
        except Exception as e: print(f"Error executing action: {e}")

    def execute_item(self, item):
        self.hide_window()
        try:
            item_path = item.get('exec_path', item['path']); item_type = item.get('type')
            if item_type in ["Calculation", "Clipboard History", "System Info"]: pyperclip.copy(item_path)
            elif item_type in ["System Command", "Shell Command"]: subprocess.run(item_path, shell=True)
            elif item_type == "Web Search": webbrowser.open(item_path)
            elif item_type == "Running Process": psutil.Process(item_path).kill()
            elif item_type in ["Application", "File", "PINNED"]:
                if not os.path.exists(item_path): print(f"Error: Path does not exist -> {item_path}"); return
                if item_path.lower().endswith(".lnk"):
                    shell = win32com.client.Dispatch("WScript.Shell"); os.startfile(shell.CreateShortCut(item_path).TargetPath)
                else: os.startfile(item_path)
        except Exception as e: print(f"Error: {e}")

    def show_window(self):
        if self.is_window_visible: return
        self.is_window_visible = True; width, height = 900, 580; x = (self.root.winfo_screenwidth() // 2) - (width // 2); y = (self.root.winfo_screenheight() // 3) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}'); self.shadow.geometry(f'{width}x{height}+{x+5}+{y+5}')
        self.root.deiconify(); self.shadow.deiconify(); self.entry.focus_force()
        if self.services.needs_reindex: self.services.start_reindex_thread()
        self.root.after(250, self.check_focus)

    def hide_window(self, event=None):
        if not self.is_window_visible: return
        self.is_window_visible = False; self.in_action_menu = False
        self.root.withdraw(); self.shadow.withdraw()
        self.entry_var.set(""); self.placeholder_label.config(text=self.placeholder_texts[self.placeholder_index])
        self.placeholder_label.place(x=5, y=5, anchor='nw')
        self.placeholder_index = (self.placeholder_index + 1) % len(self.placeholder_texts)
        for widget in self.results_frame.winfo_children(): widget.destroy()

    def get_system_info(self):
        results = []
        try: results.append({"name": socket.gethostname(), "path": "Hostname", "type": "System Info", "score": 101, "exec_path": socket.gethostname()})
        except: pass
        try: results.append({"name": socket.gethostbyname(socket.gethostname()), "path": "Local IP Address", "type": "System Info", "score": 101, "exec_path": socket.gethostbyname(socket.gethostname())})
        except: pass
        return results

def start_mouse_listener(app_instance):
    def on_move(x, y):
        if (x >= app_instance.root.winfo_screenwidth() - HOT_CORNER_SENSITIVITY and y >= app_instance.root.winfo_screenheight() - HOT_CORNER_SENSITIVITY):
            app_instance.root.after(0, app_instance.show_window)
    with mouse.Listener(on_move=on_move) as listener: listener.join()

def main():
    root = tk.Tk()
    background_services = BackgroundServices()
    app = FluentHubApp(root, background_services)
    listener_thread = threading.Thread(target=start_mouse_listener, args=(app,), daemon=True)
    listener_thread.start()
    print("Fluent Hub Command Center is running. Move mouse to bottom-right to activate.")
    print("Press Ctrl+C in this terminal to stop the script.")
    try: root.mainloop()
    except KeyboardInterrupt: print("\nScript stopped by user."); root.destroy()

if __name__ == "__main__":
    main()
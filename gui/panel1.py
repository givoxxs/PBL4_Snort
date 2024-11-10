import tkinter as tk
from tkinter import ttk
import os

style = ttk.Style()
style.configure("TButton", background="lightgrey")
style.configure("Highlighted.TButton", background="blue", foreground="white")
class Panel1(tk.Frame):
    def __init__(self, parent_frame):
        # self.parent_frame = parent_frame
        super().__init__(parent_frame) 
        self.show_panel()

    def show_panel(self):
        # Fetch and display system status
        result = os.popen("sudo ufw status numbered").read() + "\n" + os.popen("sudo systemctl status snort3-nids").read()
        label = ttk.Label(self, text=result)
        label.pack(expand=False, fill="both")
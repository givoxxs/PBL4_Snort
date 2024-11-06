import tkinter as tk
from tkinter import ttk
from gui import Panel1, Panel2, Panel3
from config.settings import config

class IDSApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Intrusion Detection System")
        self.setup_ui()

    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)
        frame4 = ttk.Frame(notebook)

        notebook.add(frame1, text="Status")
        notebook.add(frame2, text="Logs")
        notebook.add(frame3, text="Threats")
        notebook.add(frame4, text="Reload")
        notebook.pack(expand=True, fill="both")

        Panel1(frame1)
        Panel2(frame2, config.LOG_PATH)
        Panel3(frame3)
        

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = IDSApplication()
    app.run()

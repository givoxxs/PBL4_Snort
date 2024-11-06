import tkinter as tk
from tkinter import ttk
from gui import Panel1, Panel2, Panel3
from config.settings import config

class IDSApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Intrusion Detection System")
        self.root.geometry("1000x600")  # Set window size
        self.setup_ui()

    def setup_ui(self):
        # Set a modern background color for the entire app
        self.root.configure(bg="#F5F5F5")

        # Create a frame for the sidebar with a modern color
        sidebar = tk.Frame(self.root, width=200, bg="#34495E", height=600, relief="sunken", bd=0)
        sidebar.pack(side="left", fill="y")

        # Add buttons to the sidebar with modern styling
        self.button_style = {"bg": "#2C3E50", "fg": "white", "font": ("Helvetica", 12), "relief": "flat", "bd": 0, "padx": 10, "pady": 10}
        
        self.btn_status = tk.Button(sidebar, text="Status", **self.button_style, command=lambda: self.show_frame("status"))
        self.btn_logs = tk.Button(sidebar, text="Logs", **self.button_style, command=lambda: self.show_frame("logs"))
        self.btn_threats = tk.Button(sidebar, text="Threats", **self.button_style, command=lambda: self.show_frame("threats"))
        self.btn_reload = tk.Button(sidebar, text="Reload", **self.button_style, command=lambda: self.show_frame("reload"))
        
        # Pack sidebar buttons
        self.btn_status.pack(fill="x", pady=10)
        self.btn_logs.pack(fill="x", pady=10)
        self.btn_threats.pack(fill="x", pady=10)
        self.btn_reload.pack(fill="x", pady=10)

        # Create a frame for content area with a modern color
        self.content_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Create the panels (hidden by default)
        self.frames = {
            "status": Panel1(self.content_frame),
            "logs": Panel2(self.content_frame, config.LOG_PATH),
            "threats": Panel3(self.content_frame),
            "reload": self.create_reload_panel()  # Create a reload panel
        }

        # Initially show the "Status" panel and highlight its button
        self.show_frame("status")

    def show_frame(self, frame_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Show the selected frame
        self.frames[frame_name].pack(fill="both", expand=True)

        # Highlight the active button in the sidebar
        self.highlight_active_button(frame_name)

    def highlight_active_button(self, active_frame):
        # Reset button styles
        self.reset_button_styles()

        # Highlight the active button
        if active_frame == "status":
            self.btn_status.config(bg="#2980B9", relief="solid", bd=2)  # Light blue background
        elif active_frame == "logs":
            self.btn_logs.config(bg="#2980B9", relief="solid", bd=2)  # Light blue background
        elif active_frame == "threats":
            self.btn_threats.config(bg="#2980B9", relief="solid", bd=2)  # Light blue background
        elif active_frame == "reload":
            self.btn_reload.config(bg="#2980B9", relief="solid", bd=2)  # Light blue background

    def reset_button_styles(self):
        # Reset all buttons to default style
        self.btn_status.config(bg="#2C3E50", relief="flat", bd=0)
        self.btn_logs.config(bg="#2C3E50", relief="flat", bd=0)
        self.btn_threats.config(bg="#2C3E50", relief="flat", bd=0)
        self.btn_reload.config(bg="#2C3E50", relief="flat", bd=0)

    def create_reload_panel(self):
        # Example for reload panel
        reload_frame = tk.Frame(self.content_frame, bg="#ecf0f1")
        reload_label = tk.Label(reload_frame, text="Reload the IDS system here.", font=("Helvetica", 12), bg="#ecf0f1")
        reload_label.pack(pady=20)

        # Create reload button with modern style
        reload_button = tk.Button(reload_frame, text="Reload", bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="flat", bd=0, padx=20, pady=10)
        reload_button.pack(pady=10)
        return reload_frame

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = IDSApplication()
    app.run()
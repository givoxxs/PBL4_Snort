import tkinter as tk
from tkinter import ttk
from logic import AlertLogic
from utils import Plotter

style = ttk.Style()
style.configure("TButton", background="lightgrey")
style.configure("Highlighted.TButton", background="blue", foreground="white")

class Panel2(tk.Frame):
    def __init__(self, parent_frame, alert_file_path):
        super().__init__(parent_frame)
        self.alert_logic = AlertLogic(alert_file_path)
        self.child_frame = ttk.Frame(self)
        self.child_frame.pack(fill="both", expand=True)
        self.month = "all"
        self.selected_button = None
        self.create_buttons()

    def create_buttons(self):
        items = ["Treeview", "Protocol_plot", "Month_plot"]
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack()

        self.buttons = []
        for i, item in enumerate(items):
            button = ttk.Button(
                self.button_frame, text=item, command=lambda i=i: self.display_content(i + 1)
            )
            button.grid(row=0, column=i, padx=5)
            self.buttons.append(button)

        self.text_field = tk.Entry(self.button_frame)
        self.text_field.grid(row=0, column=4, padx=5)

    def highlight_button(self, index):
        # Reset all button styles
        for button in self.buttons:
            button.config(style="TButton")

        # Highlight the selected button
        self.buttons[index].config(style="Highlighted.TButton")

    def display_content(self, item_id):
        for widget in self.child_frame.winfo_children():
            widget.destroy()

        if self.text_field.get():
            self.month = self.text_field.get()
        else:
            self.month = "all"

        # Update button highlight
        self.highlight_button(item_id - 1)

        if item_id == 1:
            self.create_treeview()
        else:
            Plotter.plot(self.child_frame, item_id, self.month)

    def create_treeview(self):
        tree = ttk.Treeview(
            self.child_frame, columns=("Timestamp", "Action", "Protocol", "Gid", "Sid", "Rev", "Message", "Service",
                                       "Source IP", "Source Port", "Destination IP", "Destination Port")
        )
        # Tree configuration (headings and columns)
        for column in tree["columns"]:
            tree.heading(column, text=column)
            tree.column(column, width=100)

        # Insert data into tree
        for i, alert in enumerate(self.alert_logic.get_alerts(self.month)):
            tree.insert("", i, text=str(i), values=alert)
        tree.pack(expand=True, fill="both")

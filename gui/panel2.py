import tkinter as tk
from tkinter import ttk
from logic.alert_logic import AlertLogic
from utils.plot import Plotter

class Panel2(tk.Frame):
    def __init__(self, parent_frame, alert_file_path):
        # self.parent_frame = parent_frame
        super().__init__(parent_frame)
        self.alert_logic = AlertLogic(alert_file_path)
        self.child_frame = ttk.Frame(self) 
        # self.child_frame = ttk.Frame(parent_frame)
        self.child_frame.pack(fill="both", expand=True)
        self.create_buttons()
        self.month = "all"

    def create_buttons(self):
        items = ["Treeview", "Protocol_plot", "Month_plot"]
        # self.button_frame = ttk.Frame(self.parent_frame)
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack()

        for i, item in enumerate(items):
            button = ttk.Button(self.button_frame, text=item, command=lambda i=i: self.display_content(i + 1))
            button.grid(row=0, column=i, padx=5)

        self.text_field = tk.Entry(self.button_frame)
        self.text_field.grid(row=0, column=4, padx=5)

    def display_content(self, item_id):
        for widget in self.child_frame.winfo_children():
            widget.destroy()

        if self.text_field.get():
            self.month = self.text_field.get()
        else:
            self.month = "all"

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


# gui/panel3.py
import tkinter as tk
from tkinter import ttk
from logic.threat_logic import ThreatLogic

class Panel3(tk.Frame):
    def __init__(self, parent_frame):
        # self.parent_frame = parent_frame
        super().__init__(parent_frame)
        self.create_ui()

    def create_ui(self):
        # Use self instead of self.parent_frame since Panel3 is now a frame itself
        tree = ttk.Treeview(self, columns=("Source IP", "Destination IP", "Protocol", "Occurrence"))
        # tree = ttk.Treeview(self.parent_frame, columns=("Source IP", "Destination IP", "Protocol", "Occurrence"))
        for column in tree["columns"]:
            tree.heading(column, text=column)
            tree.column(column, width=120)
        
        # Insert mock data for testing
        for i in range(10):
            tree.insert("", "end", text=str(i), values=(f"192.168.1.{i}", f"10.0.0.{i}", "TCP", 10))

        tree.pack(expand=True, fill="both")
        self.add_buttons(tree)

    def add_buttons(self, tree):
        # button_frame = ttk.Frame(self.parent_frame)
        button_frame = ttk.Frame(self)
        button_frame.pack()

        # Create action buttons
        actions = [("Safe", ThreatLogic.safe_threat), 
                   ("Ignore", ThreatLogic.ignore_threat),
                   ("Limit", ThreatLogic.limit_threat), 
                   ("Block", ThreatLogic.block_threat)]

        for i, (text, action) in enumerate(actions):
            button = ttk.Button(button_frame, text=text, command=lambda t=tree, a=action: self.handle_action(t, a))
            button.grid(row=0, column=i, padx=5)

    def handle_action(self, tree, action):
        selected_items = tree.selection()
        if selected_items:
            selected_index = tree.index(selected_items[0])
            result = action(selected_index)
            print(result)
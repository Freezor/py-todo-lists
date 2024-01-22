# src/ui/gui_ui.py
import tkinter as tk
from tkinter import messagebox


class MainUI:
    def __init__(self, todolist):
        self.todolist = todolist

        self.root = tk.Tk()
        self.root.title("ToDo-Liste")

        self.title_entry = tk.Entry(self.root, width = 40)
        self.desc_entry = tk.Entry(self.root, width = 40)
        self.task_listbox = tk.Listbox(self.root, height = 10, selectmode = tk.SINGLE)

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text = "Titel:").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "e")
        self.title_entry.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "ew")

        tk.Label(self.root, text = "Beschreibung:").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "e")
        self.desc_entry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "ew")

        tk.Button(self.root, text = "Hinzufügen", command = self.add_task).grid(row = 2, column = 0, columnspan = 2,
                                                                                pady = 10, sticky = "ew")

        tk.Label(self.root, text = "Aufgabenliste:").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "e")
        self.task_listbox.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")

        tk.Button(self.root, text = "Als erledigt markieren", command = self.mark_as_done).grid(row = 4, column = 0,
                                                                                                columnspan = 2,
                                                                                                pady = 10,
                                                                                                sticky = "ew")
        tk.Button(self.root, text = "Entfernen", command = self.remove_task).grid(row = 5, column = 0, columnspan = 2,
                                                                                  pady = 10, sticky = "ew")

        # Configure resizing behavior
        self.root.grid_rowconfigure(3, weight = 1)
        self.root.grid_columnconfigure(1, weight = 1)

        self.refresh_task_list()

    def add_task(self):
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title == "" or description == "":
            messagebox.showwarning("Fehler bei der Dateneingabe", "Titel oder Beschreibung sind nicht gesetzt")
        else:
            self.todolist.add_task(title, description)
            self.refresh_task_list()

    def mark_as_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.todolist.mark_as_done(selected_index[0] + 1)
            self.refresh_task_list()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.todolist.remove_task(selected_index[0] + 1)
            self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.todolist.show_tasks().split("\n")
        for task in tasks:
            if task:
                self.task_listbox.insert(tk.END, task)

    def run(self):
        self.root.mainloop()

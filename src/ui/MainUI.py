import tkinter as tk
from tkinter import messagebox

from src.ui.ArchiveWindow import ArchiveWindow


class MainUI:
    """
    Represents the main user interface for a to-do list application.

    :param todo_list: The to-do list object.
    :returns: None
    """

    def __init__(self, todo_list):
        """
        Initializes a MainUI instance.

        :param todo_list: The to-do list object.
        :returns: None
        """
        self.todo_list = todo_list

        self.todo_list.load_tasks()
        self.todo_list.load_archive()

        self.root = tk.Tk()
        self.root.title("ToDo-List")

        self.root.geometry("600x800")
        self.title_entry = tk.Entry(self.root, width=40)
        self.desc_entry = tk.Entry(self.root, width=40)
        self.task_listbox = tk.Listbox(self.root, height=10, selectmode=tk.SINGLE)
        tk.Button(self.root, text="Show Archive", command=self.show_archive_window).grid(row=6, column=0,
                                                                                          columnspan=2,
                                                                                          pady=10,
                                                                                          sticky="ew")

        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface components.

        :returns: None
        """
        tk.Label(self.root, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.title_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        tk.Label(self.root, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=2, column=0, columnspan=2,
                                                                          pady=10, sticky="ew")

        tk.Label(self.root, text="Task List:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.task_listbox.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        tk.Button(self.root, text="Mark as Done", command=self.mark_as_done).grid(row=4, column=0,
                                                                                 columnspan=2,
                                                                                 pady=10,
                                                                                 sticky="ew")
        tk.Button(self.root, text="Remove", command=self.remove_task).grid(row=5, column=0, columnspan=2,
                                                                          pady=10, sticky="ew")

        # Configure resizing behavior
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.refresh_task_list()

    def add_task(self):
        """
        Adds a new task to the to-do list.

        :returns: None
        """
        title = self.title_entry.get()
        description = self.desc_entry.get()
        if title == "" or description == "":
            messagebox.showwarning("Input Error", "Title or description is not set")
        else:
            self.todo_list.add_task(title, description)
            self.refresh_task_list()

    def mark_as_done(self):
        """
        Marks the selected task as done.

        :returns: None
        """
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.todo_list.mark_as_done(selected_index[0] + 1)
            self.refresh_task_list()

    def remove_task(self):
        """
        Removes the selected task.

        :returns: None
        """
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.todo_list.remove_task(selected_index[0] + 1)
            self.refresh_task_list()

    def refresh_task_list(self):
        """
        Refreshes the task list displayed in the UI.

        :returns: None
        """
        self.task_listbox.delete(0, tk.END)
        tasks = self.todo_list.show_tasks().split("\n")
        for task in tasks:
            if task:
                self.task_listbox.insert(tk.END, task)

    def run(self):
        """
        Runs the main UI loop.

        :returns: None
        """
        self.root.mainloop()

    def show_archive_window(self):
        """
        Displays the archive window.

        :returns: None
        """
        archive_window = ArchiveWindow(self.todo_list)
        archive_window.mainloop()

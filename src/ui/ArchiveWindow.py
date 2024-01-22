import tkinter as tk
from tkinter import messagebox


class ArchiveWindow(tk.Toplevel):
    def __init__(self, todolist):
        super().__init__()
        self.title("Archiv")
        self.todolist = todolist

        self.archive_text = tk.Text(self, height=10, width=40)
        self.archive_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Bind the window resizing event to the update_size function
        self.bind("<Configure>", self.update_size)
        self.geometry("400x300")
        self.show_archive()

    def show_archive(self):
        archive_content = self.todolist.show_archive()
        self.archive_text.insert(tk.END, archive_content)
        self.archive_text.config(state=tk.DISABLED)  # Make the text widget read-only

    def update_size(self, event):
        # Adjust the size of the Text widget when the window is resized
        self.archive_text.config(width=event.width // 8, height=event.height // 20)

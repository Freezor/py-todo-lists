import tkinter as tk


class ArchiveWindow(tk.Toplevel):
    """
    Represents a window displaying the archive of a to-do list.

    :param todo_list: The to-do list object.
    :returns: None
    """

    def __init__(self, todo_list):
        """
        Initializes an ArchiveWindow instance.

        :param todo_list: The to-do list object.
        :returns: None
        """
        super().__init__()
        self.title("Archive")
        self.todo_list = todo_list

        self.archive_text = tk.Text(self, height = 10, width = 40)
        self.archive_text.pack(expand = True, fill = tk.BOTH, padx = 10, pady = 10)

        # Bind the window resizing event to the update_size function
        self.bind("<Configure>", self.update_size)
        self.geometry("600x300")
        self.display_archive()

    def display_archive(self):
        """
        Displays the archive content in the Text widget.

        :returns: None
        """
        archive_content = self.todo_list.show_archive()
        self.archive_text.insert(tk.END, archive_content)
        self.archive_text.config(state = tk.DISABLED)  # Make the text widget read-only

    def update_size(self, event):
        """
        Adjusts the size of the Text widget when the window is resized.

        :param event: The resizing event.
        :returns: None
        """
        self.archive_text.config(width = event.width // 8, height = event.height // 20)

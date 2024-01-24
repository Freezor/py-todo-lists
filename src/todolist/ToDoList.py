from src.todolist.ArchiveManager import ArchiveManager
from src.todolist.TaskManager import TaskManager


class ToDoList:
    """
    Class representing a to-do list with task and archive management.

    :returns: None
    """

    def __init__(self):
        """
        Initializes an instance of ToDoList.

        :returns: None
        """
        self.task_manager = TaskManager()
        self.archive_manager = ArchiveManager()

    def add_task(self, title, description=None):
        """
        Adds a new task to the to-do list.

        :param title: Title of the task.
        :param description: Description of the task (optional).
        :returns: None
        """
        self.task_manager.add_task(title, description)
        self.task_manager.save_tasks()

    def show_tasks(self):
        """
        Retrieves a string representation of the current tasks.

        :returns: A string containing the tasks and their details.
        """
        return self.task_manager.show_tasks()

    def mark_as_done(self, task_index):
        """
        Marks a task as done.

        :param task_index: Index of the task to be marked as done.
        :returns: None
        """
        self.task_manager.mark_as_done(task_index)
        self.task_manager.save_tasks()

    def remove_task(self, task_index):
        """
        Removes a task from the to-do list and archives it.

        :param task_index: Index of the task to be removed.
        :returns: None
        """
        removed_task = self.task_manager.remove_task(task_index)
        self.archive_manager.remove_and_archive_task(removed_task)
        self.task_manager.save_tasks()
        self.archive_manager.save_archive()

    def show_archive(self):
        """
        Retrieves a string representation of the archived tasks.

        :returns: A string containing the archived tasks and their details.
        """
        return self.archive_manager.show_archive()

    def load_tasks(self):
        """
        Loads tasks from the stored data.

        :returns: None
        """
        self.task_manager.load_tasks()

    def load_archive(self):
        """
        Loads archived tasks from the stored data.

        :returns: None
        """
        self.archive_manager.load_archive()

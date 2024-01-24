import csv
from datetime import datetime
from src.DateTimeUtils import parse_datetime_with_microseconds


class TaskManager:
    """
    Class for managing tasks within a to-do list.

    :returns: None
    """

    def __init__(self):
        """
        Initializes an instance of TaskManager.

        :returns: None
        """
        self.tasks = []

    def add_task(self, title, description=None):
        """
        Adds a new task to the list.

        :param title: Title of the task.
        :param description: Description of the task (optional).
        :returns: None
        """
        task = {"title": title, "description": description, "done": False, "created_at": datetime.now()}
        self.tasks.append(task)

    def show_tasks(self):
        """
        Generates a string representation of the tasks.

        :returns: A string containing the tasks and their details.
        """
        if not self.tasks:
            return "Keine Aufgaben vorhanden."
        tasks_str = ""
        for index, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else " "
            created_at = task["created_at"].strftime("%Y-%m-%d %H:%M:%S")
            tasks_str += f"{index}. [{status}] {task['title']} - {task['description']} (Erstellt am: {created_at})\n"
        return tasks_str

    def mark_as_done(self, task_index):
        """
        Marks a task as done.

        :param task_index: Index of the task to be marked as done.
        :returns: None
        """
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True

    def remove_task(self, task_index):
        """
        Removes a task from the list.

        :param task_index: Index of the task to be removed.
        :returns: The removed task.
        """
        if 1 <= task_index <= len(self.tasks):
            return self.tasks.pop(task_index - 1)

    def  save_tasks(self):
        """
        Saves the tasks to a CSV file.

        :returns: None
        """
        with open('tasks.csv', 'w', newline='') as csvfile:
            fieldnames = ["title", "description", "done", "created_at"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(self.tasks)

    def load_tasks(self):
        """
        Loads tasks from a CSV file.

        :returns: None
        """
        try:
            with open('tasks.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    parse_datetime_with_microseconds(row, 'created_at')
                    task = dict(row)
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

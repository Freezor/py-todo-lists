from datetime import datetime
import csv


class ToDoList:
    """
    ToDoList class represents a simple to-do list with task management functionality.

    :ivar tasks: List to store active tasks.
    :ivar archive: List to store archived tasks.

    """

    def __init__(self):
        """
        Initializes an instance of ToDoList.

        :return: None
        """
        self.tasks = []
        self.archive = []

    def add_task(self, title, description = None):
        """
        Add a new task to the to-do list.

        :param title: The title of the task.
        :param description: (Optional) Description of the task.
        :return: None
        """
        task = {"title": title, "description": description, "done": False, "created_at": datetime.now()}
        self.tasks.append(task)
        self.save_tasks()

    def show_tasks(self):
        """
        Display the list of active tasks.

        :return: A string representation of active tasks.
        """
        if not self.tasks:
            return "Keine Aufgaben vorhanden."
        tasks_str = ""
        for index, task in enumerate(self.tasks, start = 1):
            status = "✔" if task["done"] else " "
            created_at = task["created_at"].strftime("%Y-%m-%d %H:%M:%S")
            tasks_str += f"{index}. [{status}] {task['title']} - {task['description']} (Erstellt am: {created_at})\n"
        return tasks_str

    def mark_as_done(self, task_index):
        """
        Mark a specific task as done.

        :param task_index: The index of the task to mark as done.
        :return: A message indicating the result of the operation.
        """
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            self.save_tasks()
            return f"Aufgabe {task_index} als erledigt markiert."
        else:
            return "Ungültiger Index. Bitte geben Sie einen gültigen Index ein."

    def remove_task(self, task_index):
        """
        Remove a task from the active list and move it to the archive.

        :param task_index: The index of the task to remove.
        :return: A message indicating the result of the operation.
        """
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            removed_task["deleted_at"] = datetime.now()
            self.archive.append(removed_task)
            self.save_tasks()
            self.save_archive()
            return f"Aufgabe {task_index} wurde entfernt."
        else:
            return "Ungültiger Index. Bitte geben Sie einen gültigen Index ein."

    def show_archive(self):
        """
        Display the list of archived tasks.

        :return: A string representation of archived tasks.
        """
        if not self.archive:
            return "Archiv ist leer."
        archive_str = ""
        for index, task in enumerate(self.archive, start = 1):
            deleted_at = task.get("deleted_at", "N/A")
            deleted_at_str = deleted_at.strftime("%Y-%m-%d %H:%M:%S") if deleted_at != "N/A" else "N/A"
            archive_str += f"{index}. {task['title']} - {task['description']} (Gelöscht am: {deleted_at_str})\n"
        return archive_str

    def save_tasks(self):
        """
        Save active tasks to the 'tasks.csv' file.

        :return: None
        """
        with open('tasks.csv', 'w', newline = '') as csvfile:
            fieldnames = ["title", "description", "done", "created_at"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')
            writer.writeheader()
            writer.writerows(self.tasks)

    def load_tasks(self):
        """
        Load active tasks from the 'tasks.csv' file.

        :return: None
        """
        try:
            with open('tasks.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ';')
                for row in reader:
                    self._handle_date_microseconds(row, 'created_at')
                    self.tasks.append(dict(row))
        except FileNotFoundError:
            pass

    def save_archive(self):
        """
        Save archived tasks to the 'archive.csv' file.

        :return: None
        """
        with open('archive.csv', 'w', newline = '') as csvfile:
            fieldnames = ["title", "description", "done", "created_at", "deleted_at"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')
            writer.writeheader()
            writer.writerows(self.archive)

    def load_archive(self):
        """
        Load archived tasks from the 'archive.csv' file.

        :return: None
        """
        try:
            with open('archive.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ';')
                for row in reader:
                    self._handle_date_microseconds(row, 'deleted_at')
                    self.archive.append(dict(row))
        except FileNotFoundError:
            pass

    @staticmethod
    def _handle_date_microseconds(row, key):
        """
        Handle microseconds in the date string.

        :param row: The dictionary containing the row data.
        :param key: The key of the date field.
        :return: None
        """
        date_string = row[key]
        if '.' in date_string:
            date_format = "%Y-%m-%d %H:%M:%S.%f"
        else:
            date_format = "%Y-%m-%d %H:%M:%S"
        row[key] = datetime.strptime(date_string, date_format)

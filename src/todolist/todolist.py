from datetime import datetime
import csv


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.archive = []

    def add_task(self, title, description = None):
        task = {"title": title, "description": description, "done": False, "created_at": datetime.now()}
        self.tasks.append(task)
        self.save_tasks()

    def show_tasks(self):
        if not self.tasks:
            return "Keine Aufgaben vorhanden."
        else:
            tasks_str = ""
            for index, task in enumerate(self.tasks, start = 1):
                status = "✔" if task["done"] else " "
                created_at = task["created_at"].strftime("%Y-%m-%d %H:%M:%S")
                tasks_str += f"{index}. [{status}] {task['title']} - {task['description']} (Erstellt am: {created_at})\n"
            return tasks_str

    def mark_as_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            self.save_tasks()
            return f"Aufgabe {task_index} als erledigt markiert."
        else:
            return "Ungültiger Index. Bitte geben Sie einen gültigen Index ein."

    def remove_task(self, task_index):
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
        if not self.archive:
            return "Archiv ist leer."
        else:
            archive_str = ""
            for index, task in enumerate(self.archive, start = 1):
                deleted_at = task.get("deleted_at", "N/A")
                deleted_at_str = deleted_at.strftime("%Y-%m-%d %H:%M:%S") if deleted_at != "N/A" else "N/A"
                archive_str += f"{index}. {task['title']} - {task['description']} (Gelöscht am: {deleted_at_str})\n"
            return archive_str

    def save_tasks(self):
        with open('tasks.csv', 'w', newline = '') as csvfile:
            fieldnames = ["title", "description", "done", "created_at"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')
            writer.writeheader()
            writer.writerows(self.tasks)

    def load_tasks(self):
        try:
            with open('tasks.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ';')
                for row in reader:
                    # Handle microseconds in the date string
                    date_string = row['created_at']
                    if '.' in date_string:
                        date_format = "%Y-%m-%d %H:%M:%S.%f"
                    else:
                        date_format = "%Y-%m-%d %H:%M:%S"
                    row['created_at'] = datetime.strptime(date_string, date_format)
                    self.tasks.append(dict(row))
        except FileNotFoundError:
            pass

    def save_archive(self):
        with open('archive.csv', 'w', newline = '') as csvfile:
            fieldnames = ["title", "description", "done", "created_at", "deleted_at"]
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = ';')
            writer.writeheader()
            writer.writerows(self.archive)

    def load_archive(self):
        try:
            with open('archive.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ';')
                for row in reader:
                    deleted_at_string = row.get('deleted_at', 'N/A')
                    if deleted_at_string != 'N/A':
                        # Handle microseconds in the date string
                        if '.' in deleted_at_string:
                            date_format = "%Y-%m-%d %H:%M:%S.%f"
                        else:
                            date_format = "%Y-%m-%d %H:%M:%S"
                        row['deleted_at'] = datetime.strptime(deleted_at_string, date_format)
                    self.archive.append(dict(row))
        except FileNotFoundError:
            pass

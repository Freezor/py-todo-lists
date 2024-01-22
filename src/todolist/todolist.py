from datetime import datetime


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.archive = []

    def add_task(self, title, description = None):
        task = {"title": title, "description": description, "done": False, "created_at": datetime.now()}
        self.tasks.append(task)

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
            return f"Aufgabe {task_index} als erledigt markiert."
        else:
            return "Ungültiger Index. Bitte geben Sie einen gültigen Index ein."

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            removed_task["deleted_at"] = datetime.now()
            self.archive.append(removed_task)
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

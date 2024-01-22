class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description = None):
        task = {"title": title, "description": description, "done": False}
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            return "Keine Aufgaben vorhanden."
        else:
            tasks_str = ""
            for index, task in enumerate(self.tasks, start = 1):
                status = "✔" if task["done"] else " "
                tasks_str += f"{index}. [{status}] {task['title']} - {task['description']}\n"
            return tasks_str

    def mark_as_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            return f"Aufgabe {task_index} als erledigt markiert."
        else:
            return "Ungültiger Index. Bitte geben Sie einen gültigen Index ein."

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            return f"Aufgabe {task_index} wurde entfernt."
        else:
            return "Ungültiger Index. Bitte geben Sie einen gültigen Index ein."

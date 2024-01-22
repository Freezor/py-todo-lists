import csv
from datetime import datetime
from src.DateTimeUtils import DateTimeUtils


class ArchiveManager:
    """
    Class for managing archived tasks within the to-do list.

    :returns: None
    """

    def __init__(self):
        """
        Initializes an instance of ArchiveManager.

        :returns: None
        """
        self.archive = []

    def remove_and_archive_task(self, removed_task):
        """
        Archives a removed task by adding deletion timestamp.

        :param removed_task: Task to be archived.
        :returns: None
        """
        removed_task["deleted_at"] = datetime.now()
        self.archive.append(removed_task)

    def show_archive(self):
        """
        Generates a string representation of the archived tasks.

        :returns: A string containing the archived tasks and their details.
        """
        if not self.archive:
            return "Archiv ist leer."
        archive_str = ""
        for index, task in enumerate(self.archive, start=1):
            deleted_at = task.get("deleted_at", "N/A")
            deleted_at_str = deleted_at.strftime("%Y-%m-%d %H:%M:%S") if deleted_at != "N/A" else "N/A"
            archive_str += f"{index}. {task['title']} - {task['description']} (Gelöscht am: {deleted_at_str})\n"
        return archive_str

    def save_archive(self):
        """
        Saves the archived tasks to a CSV file.

        :returns: None
        """
        with open('archive.csv', 'w', newline='') as csvfile:
            fieldnames = ["title", "description", "done", "created_at", "deleted_at"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(self.archive)

    def load_archive(self):
        """
        Loads archived tasks from a CSV file.

        :returns: None
        """
        try:
            with open('archive.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ';')
                for row in reader:
                    DateTimeUtils.handle_date_microseconds(row, 'deleted_at')
                    self.archive.append(dict(row))
        except FileNotFoundError:
            pass


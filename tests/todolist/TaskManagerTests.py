import unittest
from datetime import datetime
from unittest.mock import patch, mock_open
from assertpy import assert_that

from src.todolist.TaskManager import TaskManager


class TaskManagerTests(unittest.TestCase):
    @patch("src.todolist.TaskManager.datetime")
    def test_add_task_with_default_description_should_add_task_to_task_manager(self, mock_datetime):
        # Arrange
        expected_datetime = datetime(2022, 1, 1, 12, 0, 0)
        mock_datetime.now.return_value = expected_datetime
        task_manager = TaskManager()

        # Act
        task_manager.add_task("Test Task", "Description")

        # Assert
        assert_that(task_manager.tasks).is_length(1)
        assert_that(task_manager.tasks[0]["title"]).is_equal_to("Test Task")
        assert_that(task_manager.tasks[0]["description"]).is_equal_to("Description")
        assert_that(task_manager.tasks[0]["created_at"]).is_equal_to(expected_datetime)
        assert_that(task_manager.tasks[0]["done"]).is_false()

    def test_show_tasks_empty_list_should_return_empty_message(self):
        # Arrange
        task_manager = TaskManager()

        # Act
        result = task_manager.show_tasks()

        # Assert
        assert_that(result).is_equal_to("Keine Aufgaben vorhanden.")

    def test_show_tasks_with_tasks_should_return_formatted_task_list(self):
        # Arrange
        task_manager = TaskManager()
        task_manager.tasks = [
            {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": datetime(2022, 1, 1, 12, 0, 0)},
            {"title": "Task 2", "description": "Desc 2", "done": True, "created_at": datetime(2022, 1, 2, 12, 0, 0)}
        ]

        # Act
        result = task_manager.show_tasks()

        # Assert
        assert_that(result).contains("1. [ ] Task 1 - Desc 1 (Erstellt am: 2022-01-01 12:00:00)")
        assert_that(result).contains("2. [✔] Task 2 - Desc 2 (Erstellt am: 2022-01-02 12:00:00)")

    def test_mark_as_done_valid_index_should_mark_task_as_done(self):
        # Arrange
        task_manager = TaskManager()
        task_manager.tasks = [
            {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": datetime(2022, 1, 1, 12, 0, 0)},
            {"title": "Task 2", "description": "Desc 2", "done": False, "created_at": datetime(2022, 1, 2, 12, 0, 0)}
        ]

        # Act
        task_manager.mark_as_done(2)

        # Assert
        assert_that(task_manager.tasks[1]["done"]).is_true()

    def test_mark_as_done_invalid_index_should_do_nothing(self):
        # Arrange
        task_manager = TaskManager()
        task_manager.tasks = [
            {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": datetime(2022, 1, 1, 12, 0, 0)},
            {"title": "Task 2", "description": "Desc 2", "done": False, "created_at": datetime(2022, 1, 2, 12, 0, 0)}
        ]

        # Act
        result = task_manager.mark_as_done(3)

        # Assert
        assert_that(result).is_none()

    def test_remove_task_valid_index_should_remove_task_from_task_manager(self):
        # Arrange
        task_manager = TaskManager()
        task_manager.tasks = [
            {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": datetime(2022, 1, 1, 12, 0, 0)},
            {"title": "Task 2", "description": "Desc 2", "done": False, "created_at": datetime(2022, 1, 2, 12, 0, 0)}
        ]

        # Act
        removed_task = task_manager.remove_task(2)

        # Assert
        assert_that(task_manager.tasks).is_length(1)
        assert_that(removed_task).is_equal_to(
            {"title": "Task 2", "description": "Desc 2", "done": False, "created_at": datetime(2022, 1, 2, 12, 0, 0)})

    def test_remove_task_invalid_index_should_do_nothing(self):
        # Arrange
        task_manager = TaskManager()
        task_manager.tasks = [
            {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": datetime(2022, 1, 1, 12, 0, 0)},
            {"title": "Task 2", "description": "Desc 2", "done": False, "created_at": datetime(2022, 1, 2, 12, 0, 0)}
        ]

        # Act
        result = task_manager.remove_task(3)

        # Assert
        assert_that(result).is_none()

    @patch("src.todolist.TaskManager.csv.DictReader")
    @patch("src.todolist.TaskManager.parse_datetime_with_microseconds")
    def test_load_tasks_file_not_found_should_not_change_task_manager(self, mock_parse_datetime, mock_dict_reader):
        # Arrange
        task_manager = TaskManager()

        with patch("builtins.open", mock_open(), create=True) as mock_file_open:
            mock_file_open.side_effect = FileNotFoundError

            # Act
            task_manager.load_tasks()

        # Assert
        mock_file_open.assert_called_once_with('tasks.csv', 'r')
        mock_dict_reader.assert_not_called()
        mock_parse_datetime.assert_not_called()

    @patch("src.todolist.TaskManager.csv.DictReader")
    @patch("builtins.open", create=True)
    @patch("src.todolist.TaskManager.parse_datetime_with_microseconds")
    def test_load_tasks_file_found_should_load_tasks_into_task_manager(self, mock_parse_datetime, mock_open, mock_dict_reader):
        # Arrange
        task_manager = TaskManager()
        mock_row = {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": "2022-01-01 12:00:00"}
        mock_dict_reader_instance = mock_dict_reader.return_value
        mock_dict_reader_instance.__iter__.return_value.__next__.return_value = mock_row

        with patch("builtins.open", mock_open(read_data="")):
            # Act
            task_manager.load_tasks()

        # Assert
        assert_that(task_manager.tasks).contains(mock_row)
        mock_open.assert_called_once_with('tasks.csv', 'r')
        mock_dict_reader.assert_called_once_with(mock_open().__enter__(), delimiter=';')
        mock_parse_datetime.assert_called_once_with(mock_row, 'created_at')
        # TODO: fix this test

    # TODO: Add tests for saving


if __name__ == '__main__':
    unittest.main()

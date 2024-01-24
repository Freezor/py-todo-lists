import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from src.todolist.ArchiveManager import ArchiveManager


class ArchiveManagerTests(unittest.TestCase):

    def setUp(self):
        self.archive_manager = ArchiveManager()

    def test_remove_and_archive_task_should_add_task_to_archive(self):
        # Arrange
        task = {"title": "Test Task", "description": "Description", "done": False, "created_at": datetime.now()}

        # Act
        self.archive_manager.remove_and_archive_task(task)

        # Assert
        self.assertEqual(len(self.archive_manager.archive), 1)

    def test_show_archive_should_return_empty_message_for_empty_archive(self):
        # Act
        result = self.archive_manager.show_archive()

        # Assert
        self.assertEqual(result, "Archiv ist leer.")

    def test_show_archive_should_return_formatted_string_for_non_empty_archive(self):
        # Arrange
        task = {"title": "Test Task", "description": "Description", "done": False, "created_at": datetime.now()}
        self.archive_manager.archive.append(task)

        # Act
        result = self.archive_manager.show_archive()

        # Assert
        self.assertIn("Test Task", result)

    @patch("src.todolist.ArchiveManager.csv.DictWriter")
    @patch("builtins.open", create = True)
    def test_save_archive_should_write_header_and_rows_to_csv_file(self, mock_open, mock_dict_writer):
        # Arrange
        self.archive_manager.archive = [
            {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": datetime.now(),
             "deleted_at": datetime.now()}
        ]

        # Act
        self.archive_manager.save_archive()

        # Assert
        mock_open.assert_called_once_with('archive.csv', 'w', newline = '')
        mock_dict_writer.assert_called_once_with(mock_open().__enter__(),
                                                 fieldnames = ["title", "description", "done", "created_at",
                                                               "deleted_at"],
                                                 delimiter = ';')
        mock_dict_writer_instance = mock_dict_writer().__enter__()
        mock_dict_writer_instance.writeheader.assert_called_once()
        mock_dict_writer_instance.writerows.assert_called_once_with(self.archive_manager.archive)

    @patch("src.todolist.ArchiveManager.csv.DictReader")
    @patch("builtins.open", create = True)
    def test_load_archive_should_load_tasks_from_csv_file(self, mock_open, mock_dict_reader):
        # Arrange
        mock_row = {"title": "Task 1", "description": "Desc 1", "done": False, "created_at": "2022-01-01 12:00:00",
                    "deleted_at": "2022-01-02 12:00:00"}
        mock_dict_reader_instance = mock_dict_reader.return_value
        mock_dict_reader_instance.__iter__.return_value.__next__.return_value = mock_row

        # Act
        self.archive_manager.load_archive()

        # Assert
        mock_open.assert_called_once_with('archive.csv', 'r')
        mock_dict_reader.assert_called_once_with(mock_open().__enter__(), delimiter = ';')
        mock_dict_reader_instance.__iter__.assert_called_once()
        mock_dict_reader_instance.__iter__.return_value.__next__.assert_called_once()
        self.assertEqual(len(self.archive_manager.archive), 1)

    @patch("builtins.open", create = True, side_effect = FileNotFoundError)
    def test_load_archive_should_not_raise_error_for_file_not_found(self, mock_open):
        # Act
        self.archive_manager.load_archive()

        # Assert
        mock_open.assert_called_once_with('archive.csv', 'r')
        self.assertEqual(len(self.archive_manager.archive), 0)


if __name__ == "__main__":
    unittest.main()

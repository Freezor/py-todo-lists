import unittest
from unittest.mock import patch, Mock
from tkinter import Tk

from src.ui.ArchiveWindow import ArchiveWindow


class ArchiveWindowTests(unittest.TestCase):
    def test_init_should_set_title_and_display_archive(self):
        # Arrange
        todo_list_mock = Mock()
        with patch("src.todolist.ArchiveWindow.ArchiveWindow.update_size"), \
             patch("src.todolist.ArchiveWindow.ArchiveWindow.display_archive") as display_archive_mock:
            # Act
            archive_window = ArchiveWindow(todo_list_mock)

        # Assert
        assert archive_window.title() == "Archive"
        display_archive_mock.assert_called_once()

    def test_display_archive_should_insert_archive_content_into_text_widget(self):
        # Arrange
        todo_list_mock = Mock()
        archive_window = ArchiveWindow(todo_list_mock)
        todo_list_mock.show_archive.return_value = "Task 1 - Desc 1\nTask 2 - Desc 2"

        # Act
        archive_window.display_archive()

        # Assert
        assert archive_window.archive_text.get("1.0", tk.END) == "Task 1 - Desc 1\nTask 2 - Desc 2"
        todo_list_mock.show_archive.assert_called_once()

    def test_update_size_should_adjust_text_widget_size_when_resized(self):
        # Arrange
        todo_list_mock = Mock()
        archive_window = ArchiveWindow(todo_list_mock)
        event_mock = Mock(width=800, height=400)

        # Act
        archive_window.update_size(event_mock)

        # Assert
        assert archive_window.archive_text.cget("width") == 100  # 800 // 8
        assert archive_window.archive_text.cget("height") == 20  # 400 // 20

    @patch("src.todolist.ArchiveWindow.ArchiveWindow.update_size")
    def test_bind_configure_event_should_bind_update_size_function(self, update_size_mock):
        # Arrange
        todo_list_mock = Mock()
        archive_window = ArchiveWindow(todo_list_mock)

        # Act
        archive_window.event_generate("<Configure>")

        # Assert
        update_size_mock.assert_called_once()

    def test_init_should_set_geometry_and_display_archive(self):
        # Arrange
        todo_list_mock = Mock()
        with patch("src.todolist.ArchiveWindow.ArchiveWindow.update_size"), \
             patch("src.todolist.ArchiveWindow.ArchiveWindow.display_archive") as display_archive_mock:
            # Act
            archive_window = ArchiveWindow(todo_list_mock)

        # Assert
        assert archive_window.geometry() == "600x300"
        display_archive_mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()

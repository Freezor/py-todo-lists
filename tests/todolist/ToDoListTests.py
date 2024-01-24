import unittest
from unittest.mock import patch, MagicMock
from assertpy import assert_that
from src.todolist.ToDoList import ToDoList


class ToDoListTests(unittest.TestCase):

    def setUp(self):
        self.todo_list = ToDoList()

    @patch.object(ToDoList, 'load_tasks')
    def test_add_task_calls_load_tasks_after_adding_task(self, mock_load_tasks):
        # Arrange
        title = "New Task"
        description = "Description"

        # Act
        self.todo_list.add_task(title, description)

        # Assert
        assert_that(mock_load_tasks.called).is_true()

    @patch.object(ToDoList, 'load_tasks')
    def test_show_tasks_calls_load_tasks(self, mock_load_tasks):
        # Act
        self.todo_list.show_tasks()

        # Assert
        assert_that(mock_load_tasks.called).is_true()

    @patch.object(ToDoList, 'load_tasks')
    def test_mark_as_done_calls_load_tasks_after_marking_task_as_done(self, mock_load_tasks):
        # Arrange
        task_index = 1

        # Act
        self.todo_list.mark_as_done(task_index)

        # Assert
        assert_that(mock_load_tasks.called).is_true()

    @patch.object(ToDoList, 'load_tasks')
    def test_remove_task_calls_load_tasks_after_removing_task(self, mock_load_tasks):
        # Arrange
        task_index = 1

        # Act
        self.todo_list.remove_task(task_index)

        # Assert
        assert_that(mock_load_tasks.called).is_true()

    @patch.object(ToDoList, 'load_archive')
    def test_show_archive_calls_load_archive(self, mock_load_archive):
        # Act
        self.todo_list.show_archive()

        # Assert
        assert_that(mock_load_archive.called).is_true()

    @patch("src.todolist.ToDoList.TaskManager")
    @patch("src.todolist.ToDoList.ArchiveManager")
    def test_load_tasks_calls_load_tasks_on_task_manager(self, mock_task_manager, mock_archive_manager):
        # Arrange
        todo_list = ToDoList()

        # Act
        todo_list.load_tasks()

        # Assert
        assert_that(mock_task_manager.return_value.load_tasks.called).is_true()

    @patch("src.todolist.ToDoList.ArchiveManager")
    def test_load_archive_calls_load_archive_on_archive_manager(self, mock_archive_manager):
        # Arrange
        todo_list = ToDoList()

        # Act
        todo_list.load_archive()

        # Assert
        assert_that(mock_archive_manager.return_value.load_archive.called).is_true()


if __name__ == "__main__":
    unittest.main()

from src.todolist.todolist import ToDoList
from src.ui.MainUI import MainUI

if __name__ == "__main__":
    todo_list = ToDoList()
    gui_ui = MainUI(todo_list)
    gui_ui.run()

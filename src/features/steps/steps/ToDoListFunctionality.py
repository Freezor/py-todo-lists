import lettuce
from behave import given, when, then
from src.todolist.ToDoList import ToDoList
from src.todolist.ArchiveManager import ArchiveManager
from src.todolist.TaskManager import TaskManager


@given('the ToDo list is empty')
def step_given_todo_list_empty(context):
    context.task_manager = TaskManager()


@given('the ToDo list contains a task "{title}"')
def step_given_todo_list_contains(context, title):
    context.task_manager = TaskManager()
    context.task_manager.add_task(title)
    tasks = context.task_manager.show_tasks()
    assert title in tasks, f'Task "{title}" not found in ToDo list'


@when('I add a task with title "{title}" and description "{description}"')
def step_when_add_task(context, title, description):
    context.task_manager.add_task(title, description)


@then('the ToDo list should contain "{title}"')
def step_then_todo_list_contains(context, title):
    tasks = context.task_manager.show_tasks()
    assert title in tasks, f'Task "{title}" not found in ToDo list'


@given('the ToDo list contains a task "{title}" marked as not done')
def step_given_todo_list_contains_not_done(context, title):
    context.task_manager.add_task(title)
    tasks = context.task_manager.show_tasks()
    assert title in tasks, f'Task "{title}" not found in ToDo list'
    assert 'Done' not in tasks, f'Task "{title}" should not be marked as done'


@given('the ToDo list contains a task "{title}" marked as done')
def step_given_todo_list_contains_done(context, title):
    context.task_manager.add_task(title)
    context.task_manager.mark_as_done(0)
    tasks = context.task_manager.show_tasks()
    assert title in tasks, f'Task "{title}" not found in ToDo list'
    assert 'Done' in tasks, f'Task "{title}" should be marked as done'


@when('I mark the task as done')
def step_when_mark_task_done(context):
    context.task_manager.mark_as_done(0)


@then('the ToDo list should contain a task "{title}" marked as done')
def step_then_todo_list_contains_done(context, title):
    tasks = context.todo_list.show_tasks()
    assert title in tasks, f'Task "{title}" not found in ToDo list'
    assert f'✔ {title}' in tasks, f'Task "{title}" should be marked as done'


@when('I remove the task "{title}"')
def step_when_remove_task(context, title):
    context.task_manager.remove_task(0)


@then('the ToDo list should not contain a task "{title}"')
def step_then_todo_list_not_contains(context, title):
    tasks = context.task_manager.show_tasks()
    assert title not in tasks, f'Task "{title}" still found in ToDo list'


@when('I load tasks from a saved state with tasks:')
def step_when_load_tasks_from_saved_state(context):
    tasks_table = context.table
    context.todo_list = ToDoList()
    for row in tasks_table.rows:
        context.todo_list.task_manager.add_task(row['title'], row['description'])
        if row['done'].lower() == 'true':
            context.todo_list.task_manager.mark_as_done(0)


@then('the Archive should contain a task "{title}" marked as done')
def step_then_archive_contains_done(context, title):
    archive = context.task_manager.show_archive()
    assert title in archive, f'Task "{title}" not found in Archive'
    assert 'Done' in archive, f'Task "{title}" should be marked as done in Archive'


@then('the ToDo list should contain a task "{title}" marked as not done')
def step_then_todo_list_contains_not_done(context, title):
    tasks = context.task_manager.show_tasks()
    assert title in tasks, f'Task "{title}" not found in ToDo list'
    assert 'Done' not in tasks, f'Task "{title}" should not be marked as done in ToDo list'

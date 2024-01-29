from behave import given, when, then, register_type

@given('the ToDo list is empty')
def step_given_todo_list_empty(context):
    context.todo_list = []


@when('I add a task with title "{title}" and description "{description}"')
def step_when_add_task(context, title, description):
    task = {'title': title, 'description': description, 'done': False}
    context.todo_list.append(task)


@then('the ToDo list should contain "{title}"')
def step_then_todo_list_contains(context, title):
    assert any(task['title'] == title for task in context.todo_list), f'Task "{title}" not found'


@given('the ToDo list contains a task "{title}"')
def step_given_todo_list_contains(context, title):
    context.todo_list = [{'title': title, 'done': False}]


@when('I mark the task as done')
def step_when_mark_task_done(context):
    context.todo_list[0]['done'] = True


@then('the ToDo list should contain a task "{title}" marked as done')
def step_then_todo_list_contains_done(context, title):
    matching_tasks = [task for task in context.todo_list if task['title'] == title and task['done']]
    assert matching_tasks, f'No task with title "{title}" marked as done found'

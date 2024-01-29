# Created by Oliver Fries at 29.01.2024
Feature: To Do List functionality

  Scenario: Adding a task to the ToDo list
    Given the ToDo list is empty
    When I add a task with title "Buy groceries" and description "Eggs, milk, and bread"
    Then the ToDo list should contain "Buy groceries"

  Scenario: Completing a task in the ToDo list
    Given the ToDo list contains a task "Read a book"
    When I mark the task as done
    Then the ToDo list should contain a task "Read a book" marked as done

    # Try to enter an empty task, Remove a task from the list and should be shown in archive
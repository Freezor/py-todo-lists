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

  Scenario: Remove a task from the ToDo list
    Given the ToDo list contains a task "Write report" marked as not done
    When I remove the task "Write report"
    Then the ToDo list should not contain a task "Write report"

  Scenario: Archive a completed task
    Given the ToDo list contains a task "Exercise" marked as done
    When I remove the task "Exercise"
    Then the ToDo list should not contain a task "Exercise"
    And the Archive should contain a task "Exercise" marked as done

  Scenario: Load tasks from a saved state
    Given the ToDo list is empty
    When I load tasks from a saved state with tasks:
        | title           | description       | done |
        | Study Python    | Practice coding   | false|
        | Learn React      | Build a web app   | true |
    Then the ToDo list should contain a task "Study Python" marked as not done
    And the ToDo list should contain a task "Learn React" marked as done

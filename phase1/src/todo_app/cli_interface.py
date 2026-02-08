"""
CLI interface for the todo application.

Contains functions for displaying menus, getting user input,
and handling user interactions in the console.
"""

from typing import Optional

# Handle both module and direct execution
try:
    from .business_logic import TodoService
except ImportError:
    # When run directly, import from the same directory
    from business_logic import TodoService


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "="*40)
    print("         TODO APPLICATION")
    print("="*40)
    print("1. View all todos")
    print("2. Add a new todo")
    print("3. Update a todo")
    print("4. Mark a todo as complete")
    print("5. Delete a todo")
    print("0. Exit")
    print("="*40)


def get_user_choice() -> int:
    """
    Get the user's menu choice.

    Returns:
        int: The user's menu choice (0-5)
    """
    while True:
        try:
            choice = int(input("Enter your choice (0-5): "))
            if 0 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_todos(todos):
    """
    Display all todos in a formatted way.

    Args:
        todos: List of Todo objects to display
    """
    if not todos:
        print("\nNo todos found. Your list is empty!")
        return

    print(f"\n{'ID':<4} {'Status':<8} {'Title'}")
    print("-" * 40)
    for todo in todos:
        status = "✓ Done" if todo.completed else "○ Pending"
        print(f"{todo.id:<4} {status:<8} {todo.title}")


def get_todo_input(prompt: str = "Enter todo ID: ") -> int:
    """
    Get a valid todo ID from user input.

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        int: The valid todo ID entered by the user
    """
    while True:
        try:
            todo_id = int(input(prompt))
            if todo_id > 0:
                return todo_id
            else:
                print("Please enter a positive number for the todo ID.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_todo_title() -> str:
    """
    Get a todo title from user input.

    Returns:
        str: The todo title entered by the user
    """
    while True:
        title = input("Enter the todo title: ").strip()
        if title:
            return title
        else:
            print("Todo title cannot be empty. Please try again.")


def handle_view_todos(service: TodoService):
    """
    Handle the view todos functionality.

    Args:
        service (TodoService): The todo service to use
    """
    todos = service.list_todos()
    display_todos(todos)


def handle_add_todo(service: TodoService):
    """
    Handle the add todo functionality.

    Args:
        service (TodoService): The todo service to use
    """
    try:
        title = get_todo_title()
        todo = service.add_todo(title)
        print(f"✓ Successfully added todo: '{todo.title}' with ID {todo.id}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def handle_update_todo(service: TodoService):
    """
    Handle the update todo functionality.

    Args:
        service (TodoService): The todo service to use
    """
    if not service.list_todos():
        print("No todos available to update.")
        return

    todo_id = get_todo_input("Enter the ID of the todo to update: ")
    todo = service.get_todo(todo_id)

    if not todo:
        print(f"✗ Todo with ID {todo_id} not found.")
        return

    print(f"Current todo: {todo}")
    new_title = input(f"Enter new title (or press Enter to keep '{todo.title}'): ").strip()

    if not new_title:
        print("Update cancelled - no changes made.")
        return

    try:
        success = service.update_todo(todo_id, new_title)
        if success:
            print(f"✓ Successfully updated todo with ID {todo_id}")
        else:
            print(f"✗ Failed to update todo with ID {todo_id}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def handle_mark_complete(service: TodoService):
    """
    Handle the mark complete functionality.

    Args:
        service (TodoService): The todo service to use
    """
    if not service.list_todos():
        print("No todos available to mark as complete.")
        return

    todo_id = get_todo_input("Enter the ID of the todo to mark complete: ")
    success = service.mark_complete(todo_id)

    if success:
        print(f"✓ Successfully marked todo with ID {todo_id} as complete")
    else:
        print(f"✗ Todo with ID {todo_id} not found")


def handle_delete_todo(service: TodoService):
    """
    Handle the delete todo functionality.

    Args:
        service (TodoService): The todo service to use
    """
    if not service.list_todos():
        print("No todos available to delete.")
        return

    todo_id = get_todo_input("Enter the ID of the todo to delete: ")
    success = service.delete_todo(todo_id)

    if success:
        print(f"✓ Successfully deleted todo with ID {todo_id}")
    else:
        print(f"✗ Todo with ID {todo_id} not found")


def run_cli():
    """
    Run the main CLI loop for the todo application.
    """
    service = TodoService()

    print("Welcome to the Todo Application!")
    print("Manage your tasks efficiently in this console-based app.")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            handle_view_todos(service)
        elif choice == 2:
            handle_add_todo(service)
        elif choice == 3:
            handle_update_todo(service)
        elif choice == 4:
            handle_mark_complete(service)
        elif choice == 5:
            handle_delete_todo(service)
        elif choice == 0:
            print("Thank you for using the Todo Application. Goodbye!")
            break
        else:
            print("Unexpected choice. Please try again.")

        # Pause to let user see the result before showing menu again
        input("\nPress Enter to continue...")
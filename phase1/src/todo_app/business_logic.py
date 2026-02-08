"""
Business logic layer for the todo application.

Contains the TodoService class that implements the core operations
for managing todos (add, update, delete, etc.).
"""

from typing import List, Optional

# Handle both module and direct execution
try:
    from .models import Todo, TodoList
except ImportError:
    # When run directly, import from the same directory
    from models import Todo, TodoList


class TodoService:
    """
    Service class that encapsulates the business logic for todo operations.
    """

    def __init__(self):
        """Initialize the TodoService with a TodoList."""
        self.todo_list = TodoList()

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo with the given title.

        Args:
            title (str): The title/description of the new todo

        Returns:
            Todo: The newly created Todo object

        Raises:
            ValueError: If the title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty or blank")

        return self.todo_list.add_todo(title)

    def list_todos(self) -> List[Todo]:
        """
        Get all todos in the list.

        Returns:
            List[Todo]: All todos in the list
        """
        return self.todo_list.list_todos()

    def update_todo(self, todo_id: int, new_title: str = None) -> bool:
        """
        Update the title of an existing todo.

        Args:
            todo_id (int): The ID of the todo to update
            new_title (str): The new title for the todo

        Returns:
            bool: True if the todo was updated, False if not found

        Raises:
            ValueError: If the new title is empty or None
        """
        if new_title is not None:
            if not new_title or not new_title.strip():
                raise ValueError("Todo title cannot be empty or blank")

        return self.todo_list.update_todo(todo_id, new_title=new_title)

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to delete

        Returns:
            bool: True if the todo was deleted, False if not found
        """
        return self.todo_list.delete_todo(todo_id)

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as complete by its ID.

        Args:
            todo_id (int): The ID of the todo to mark complete

        Returns:
            bool: True if the todo was marked complete, False if not found
        """
        return self.todo_list.mark_complete(todo_id)

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Get a specific todo by its ID.

        Args:
            todo_id (int): The ID of the todo to retrieve

        Returns:
            Todo or None: The todo if found, None otherwise
        """
        return self.todo_list.find_todo(todo_id)
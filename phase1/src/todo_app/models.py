"""
Todo data models for the console application.

Contains the Todo and TodoList classes that represent the core data structures
for the todo application.
"""

from typing import List, Optional


class Todo:
    """
    Represents a single todo item with an ID, title, and completion status.
    """

    def __init__(self, id: int, title: str, completed: bool = False):
        """
        Initialize a Todo object.

        Args:
            id (int): Unique identifier for the todo
            title (str): Description of the todo
            completed (bool): Whether the todo is completed (default: False)
        """
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        """String representation of the todo."""
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}. {self.title}"

    def __repr__(self):
        """Developer representation of the todo."""
        return f"Todo(id={self.id}, title='{self.title}', completed={self.completed})"


class TodoList:
    """
    Container for multiple Todo items stored in memory.
    """

    def __init__(self):
        """Initialize an empty TodoList with ID counter."""
        self.todos: List[Todo] = []
        self.next_id = 1

    def add_todo(self, title: str) -> Todo:
        """
        Add a new todo to the collection with unique ID.

        Args:
            title (str): The title/description of the new todo

        Returns:
            Todo: The newly created Todo object
        """
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty")

        todo = Todo(id=self.next_id, title=title.strip())
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def find_todo(self, todo_id: int) -> Optional[Todo]:
        """
        Retrieve a todo by its ID.

        Args:
            todo_id (int): The ID of the todo to find

        Returns:
            Todo or None: The todo if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_title: str = None, completed: bool = None) -> bool:
        """
        Update an existing todo's properties.

        Args:
            todo_id (int): The ID of the todo to update
            new_title (str, optional): New title for the todo
            completed (bool, optional): New completion status for the todo

        Returns:
            bool: True if the todo was updated, False if not found
        """
        todo = self.find_todo(todo_id)
        if not todo:
            return False

        if new_title is not None:
            if not new_title or not new_title.strip():
                raise ValueError("Todo title cannot be empty")
            todo.title = new_title.strip()

        if completed is not None:
            todo.completed = completed

        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Remove a todo from the collection.

        Args:
            todo_id (int): The ID of the todo to delete

        Returns:
            bool: True if the todo was deleted, False if not found
        """
        todo = self.find_todo(todo_id)
        if not todo:
            return False

        self.todos.remove(todo)
        return True

    def list_todos(self) -> List[Todo]:
        """
        Return all todos in the collection.

        Returns:
            List[Todo]: All todos in the collection
        """
        return self.todos[:]

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a specific todo as complete.

        Args:
            todo_id (int): The ID of the todo to mark complete

        Returns:
            bool: True if the todo was marked complete, False if not found
        """
        todo = self.find_todo(todo_id)
        if not todo:
            return False

        todo.completed = True
        return True
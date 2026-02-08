# Data Model: Todo Application

## Entities

### Todo
**Description**: Represents a single task in the todo list

**Attributes**:
- `id`: integer - Unique identifier for the todo item
- `title`: string - The text description of the task
- `completed`: boolean - Status indicator showing if the task is completed

**Validation Rules**:
- `id` must be a positive integer
- `title` must be a non-empty string
- `completed` must be a boolean value (True/False)

**State Transitions**:
- `completed` can transition from False to True (mark as complete)
- `completed` cannot transition from True to False (per requirements)

### TodoList
**Description**: Container for multiple Todo items stored in memory

**Attributes**:
- `todos`: list/array - Collection of Todo objects
- `next_id`: integer - Counter for generating unique IDs for new todos

**Operations**:
- Add Todo: Adds a new Todo to the collection with unique ID
- Find Todo: Retrieves Todo by ID
- Update Todo: Modifies existing Todo properties
- Delete Todo: Removes Todo from collection
- List Todos: Returns all Todo objects in readable format

## Relationships

- TodoList contains zero-to-many Todo objects
- Each Todo has a unique ID within its TodoList

## Constraints

- No duplicate IDs within the same TodoList
- Todo titles must not be empty strings
- Todo objects must have all required attributes
- In-memory storage only (no persistence)
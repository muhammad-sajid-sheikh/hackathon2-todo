# Data Model: Todo Full-Stack Web Application

## User Entity

### Fields
- `id` (UUID/string): Unique identifier for the user
- `email` (string): User's email address (unique, required)
- `hashed_password` (string): Securely hashed password
- `created_at` (timestamp): Account creation timestamp
- `updated_at` (timestamp): Last update timestamp
- `is_active` (boolean): Account status flag

### Relationships
- One-to-many: User → Tasks (user owns multiple tasks)

### Validation Rules
- Email must be valid format and unique across all users
- Password must meet security requirements when hashing
- Email is required and cannot be empty

## Task Entity

### Fields
- `id` (UUID/string): Unique identifier for the task
- `title` (string): Task title (required, max 255 characters)
- `description` (string): Optional task description (max 1000 characters)
- `status` (enum): Task status (values: "todo", "in-progress", "completed")
- `priority` (enum): Task priority level (values: "low", "medium", "high")
- `user_id` (UUID/string): Foreign key reference to owning user
- `created_at` (timestamp): Task creation timestamp
- `updated_at` (timestamp): Last update timestamp
- `completed_at` (timestamp, nullable): Timestamp when task was marked as completed

### Relationships
- Many-to-one: Task → User (task belongs to one user)

### Validation Rules
- Title is required and cannot be empty
- User_id must reference an existing, active user
- Status must be one of the allowed enum values
- Priority must be one of the allowed enum values
- Only the owning user can modify or delete the task

## State Transitions

### Task Status Transitions
- `todo` → `in-progress`: When user begins working on task
- `in-progress` → `completed`: When user marks task as completed
- `completed` → `in-progress`: When user reopens completed task
- `in-progress` → `todo`: When user reverts task to todo state

### User Account Transitions
- `inactive` → `active`: Upon successful registration and verification
- `active` → `inactive`: When account is deactivated

## Constraints & Indexes

### Database Constraints
- `users.email` must be unique
- `tasks.user_id` must reference existing user
- `tasks.title` cannot be empty
- `tasks.status` restricted to allowed values
- `tasks.priority` restricted to allowed values

### Indexes
- `users.email`: B-tree index for authentication lookups
- `tasks.user_id`: B-tree index for user-based filtering
- `tasks.created_at`: B-tree index for chronological ordering
- `tasks.status`: B-tree index for status-based filtering
- `tasks.priority`: B-tree index for priority-based filtering

## API Access Patterns

### Expected Query Patterns
- Retrieve all tasks for a specific user: `WHERE user_id = ?`
- Retrieve tasks with specific status for a user: `WHERE user_id = ? AND status = ?`
- Retrieve tasks ordered by creation date: `ORDER BY created_at DESC`
- Retrieve tasks by priority: `WHERE user_id = ? AND priority = ?`

### Security Constraints
- Queries must always filter by `user_id` to enforce data isolation
- Only the owning user can access, modify, or delete tasks
- Foreign key constraints prevent orphaned tasks
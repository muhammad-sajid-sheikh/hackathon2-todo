# Quickstart Guide: Todo Application

## Overview
This is a console-based todo application that runs in memory with no persistence. It provides basic todo management functionality through a menu-driven interface.

## Prerequisites
- Python 3.13 or higher
- No external dependencies required

## Setup
1. Navigate to the project directory
2. Ensure Python 3.13+ is installed: `python --version`
3. Run the application: `python src/todo_app/main.py`

## Usage
1. Run the application to see the main menu
2. Select options using the numeric menu system:
   - Option 1: View all todos
   - Option 2: Add a new todo
   - Option 3: Update an existing todo
   - Option 4: Mark a todo as complete
   - Option 5: Delete a todo
   - Option 0: Exit the application

## Example Workflow
1. Run the program: `python src/todo_app/main.py`
2. Select "2" to add a new todo
3. Enter your todo description
4. Select "1" to view your todos
5. Continue using other options as needed
6. Select "0" to exit

## Features
- Add, view, update, delete, and mark complete for todos
- Input validation for all operations
- Error handling for invalid inputs
- Persistent session until user exits

## Limitations
- Data is stored only in memory
- Data is lost when application exits
- No synchronization or sharing capability
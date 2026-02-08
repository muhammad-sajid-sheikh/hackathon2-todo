---
description: "Task list for Phase I Todo Application implementation"
---

# Tasks: Phase I - In-Memory Python Console Todo App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No automated tests required - manual testing through console interaction per spec

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/todo_app/
- [x] T002 Create __init__.py file in src/todo_app/__init__.py
- [x] T003 [P] Create models.py file in src/todo_app/models.py
- [x] T004 [P] Create business_logic.py file in src/todo_app/business_logic.py
- [x] T005 [P] Create cli_interface.py file in src/todo_app/cli_interface.py
- [x] T006 [P] Create main.py file in src/todo_app/main.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Create Todo data model class in src/todo_app/models.py
- [x] T008 Create TodoList container class in src/todo_app/models.py
- [x] T009 Create TodoService with basic operations in src/todo_app/business_logic.py
- [x] T010 Create basic CLI interface functions in src/todo_app/cli_interface.py
- [x] T011 Create main application loop in src/todo_app/main.py
- [x] T012 Set up basic error handling and validation in src/todo_app/models.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with unique IDs and mark them as incomplete

**Independent Test**: Can run the app, select "Add Todo", enter a task description, and verify that the task appears in the list with a unique ID and "Incomplete" status

### Implementation for User Story 1

- [x] T013 [US1] Implement add_todo method in TodoService in src/todo_app/business_logic.py
- [x] T014 [US1] Implement add todo functionality in CLI interface in src/todo_app/cli_interface.py
- [x] T015 [US1] Add input validation for empty task descriptions in src/todo_app/business_logic.py
- [x] T016 [US1] Connect add todo functionality to main menu in src/todo_app/main.py
- [x] T017 [US1] Test adding todo functionality manually

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todos (Priority: P1)

**Goal**: Enable users to see all their current tasks with IDs, text, and completion status in a readable format

**Independent Test**: Can run the app, select "View Todos", and verify that all existing todos are displayed with their IDs, text, and completion status

### Implementation for User Story 2

- [x] T018 [US2] Implement list_todos method in TodoService in src/todo_app/business_logic.py
- [x] T019 [US2] Implement view todos functionality in CLI interface in src/todo_app/cli_interface.py
- [x] T020 [US2] Handle empty state gracefully with appropriate message in src/todo_app/cli_interface.py
- [x] T021 [US2] Connect view todos functionality to main menu in src/todo_app/main.py
- [x] T022 [US2] Test viewing todos functionality manually

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Enable users to mark a specific task as completed using its ID

**Independent Test**: Can run the app, add a todo, select "Mark Complete", enter the todo ID, and verify that the status changes to "Complete"

### Implementation for User Story 3

- [x] T023 [US3] Implement mark_complete method in TodoService in src/todo_app/business_logic.py
- [x] T024 [US3] Implement mark complete functionality in CLI interface in src/todo_app/cli_interface.py
- [x] T025 [US3] Add validation for invalid todo IDs in src/todo_app/business_logic.py
- [x] T026 [US3] Connect mark complete functionality to main menu in src/todo_app/main.py
- [x] T027 [US3] Test mark complete functionality manually

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Update Todo (Priority: P2)

**Goal**: Enable users to modify the text of an existing todo using its ID

**Independent Test**: Can run the app, add a todo, select "Update Todo", enter the todo ID and new text, and verify that the text is updated

### Implementation for User Story 4

- [x] T028 [US4] Implement update_todo method in TodoService in src/todo_app/business_logic.py
- [x] T029 [US4] Implement update todo functionality in CLI interface in src/todo_app/cli_interface.py
- [x] T030 [US4] Add validation for invalid todo IDs and empty text in src/todo_app/business_logic.py
- [x] T031 [US4] Connect update todo functionality to main menu in src/todo_app/main.py
- [x] T032 [US4] Test update todo functionality manually

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Enable users to remove a specific todo from the list using its ID

**Independent Test**: Can run the app, add a todo, select "Delete Todo", enter the todo ID, and verify that the todo is removed from the list

### Implementation for User Story 5

- [x] T033 [US5] Implement delete_todo method in TodoService in src/todo_app/business_logic.py
- [x] T034 [US5] Implement delete todo functionality in CLI interface in src/todo_app/cli_interface.py
- [x] T035 [US5] Add validation for invalid todo IDs in src/todo_app/business_logic.py
- [x] T036 [US5] Connect delete todo functionality to main menu in src/todo_app/main.py
- [x] T037 [US5] Test delete todo functionality manually

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T038 [P] Improve error messages and user feedback across all functionalities in src/todo_app/cli_interface.py
- [x] T039 [P] Add input validation for all user inputs in src/todo_app/business_logic.py
- [x] T040 [P] Handle edge cases like non-numeric IDs and special characters in src/todo_app/business_logic.py
- [x] T041 [P] Add comprehensive comments and docstrings in all modules
- [x] T042 [P] Implement graceful error handling for all operations in src/todo_app/business_logic.py
- [x] T043 Run quickstart validation to ensure all features work together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with previous stories but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement add_todo method in TodoService in src/todo_app/business_logic.py"
Task: "Implement add todo functionality in CLI interface in src/todo_app/cli_interface.py"
Task: "Connect add todo functionality to main menu in src/todo_app/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
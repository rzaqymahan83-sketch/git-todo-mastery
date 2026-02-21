# CLI Todo – Command Line Task Manager

A simple command-line to-do list application built with **Python** as a learning project.

This repository is being developed step-by-step over 12 days to practice core Python fundamentals.

## Current Status (Day 1)

- Project initialization
- Welcome message with basic formatting
- Usage of basic variable types: `str`, `int`, `float`, `bool`
- First Git commit with project structure

### Features

(Planned – being implemented day by day)

- [ ] Add new tasks with title & optional description
- [ ] List all tasks with status & basic info
- [ ] Mark tasks as completed
- [ ] Delete tasks
- [ ] Set priority level for tasks
- [ ] Persistent storage (save/load tasks using JSON file)
- [ ] Basic input validation & error messages
- [ ] Clean command-line interface with numbered menu
- [ ] Help / usage instructions inside the program

### Key Notes

- Pure Python – only using the **standard library** (no external packages)
- Project-based learning: each day adds one or more fundamental Python concept
- Focus on **readability**, **simple structure** and **good naming**
- Following official Python style guide (**PEP 8**) as much as possible
- Designed to be beginner-friendly but gradually introduces real-world patterns
- Suitable as a first portfolio project for junior Python developers
- 100% console-based (CLI) – no GUI

### Planned Learning Journey (12 days)

1. Variables & basic data types  
2. Operators & user input  
3. Conditionals (if/elif/else)  
4. Loops (for/while)  
5. Lists  
6. Tuples, Sets, Dictionaries  
7. Strings & formatting  
8. Functions  
9. Modules & code organization  
10. File I/O  
11. Exception handling  
12. Basic OOP + final refactoring

## Current Status (Day 2)

- Interactive command-line menu (1–3 options)
- User input handling with `input()`
- Basic string validation (non-empty task title)
- Simple loop for continuous program execution
- Improved welcome screen & formatting

## Features

- [ ] Add new tasks with title & optional description
- [x] Basic command-line menu interface
- [ ] List all tasks with status & basic info
- [ ] Mark tasks as completed
- [ ] Delete tasks
- [ ] Set priority level for tasks
- [ ] Persistent storage (save/load tasks using JSON file)
- [ ] Basic input validation & error messages
- [ ] Help / usage instructions inside the program

## Current Status (Day 3)

- Proper conditional logic for menu choices (if/elif/else)
- Input validation (non-empty task titles)
- Tasks stored in memory using a list
- Separated logic into small functions
- Numbered task display with `enumerate()`

## Features

- [x] Basic command-line menu interface  
- [x] Add new tasks (title only – stored in memory)  
- [x] Show all tasks (simple numbered list)  
- [ ] Mark tasks as completed  
- [ ] Delete tasks  
- [ ] Set priority level for tasks  
- [ ] Persistent storage (save/load tasks using JSON file)  
- [ ] Better input validation & friendly error messages  
- [ ] Help / usage instructions inside the program

## Current Status (Day 4)

- for loop + enumerate for numbered task listing
- while loop continues to power the main menu
- New feature: clear all tasks (with confirmation)
- Basic loop control (break when user exits)
- Added total task count display

## Features

- [x] Basic command-line menu interface  
- [x] Add new tasks (title only – stored in memory)  
- [x] Show all tasks (numbered list with enumerate)  
- [x] Clear all tasks (with user confirmation)  
- [ ] Mark tasks as completed  
- [ ] Delete single task  
- [ ] Set priority level for tasks  
- [ ] Persistent storage (save/load tasks using JSON file)  
- [ ] Better input validation & friendly error messages  
- [ ] Help / usage instructions inside the program

## Current Status (Day 5)

- Deep usage of lists: append, pop, len, enumerate
- Tasks now stored as list of dictionaries (title + done status)
- New feature: delete single task by number
- Status indicators ([ ] / [x]) in task list
- Better error handling for invalid numbers

## Features

- [x] Basic command-line menu interface  
- [x] Add new tasks  
- [x] Show all tasks (with status)  
- [x] Delete single task by number  
- [x] Clear all tasks (with confirmation)  
- [ ] Mark task as completed  
- [ ] Edit task title  
- [ ] Priority / due date  
- [ ] Save/load to file  
- [ ] Better input validation

## Current Status (Day 6)

- Usage of tuple for constant values (priority levels)
- Tasks dictionary expanded (priority field added)
- Sorting tasks by priority using sorted() + lambda + dict.get()
- Input validation loop for priority selection

## Features

- [x] Add task with priority
- [x] Show tasks sorted by priority
- [x] Delete single task
- [x] Clear all tasks
- [ ] Mark task as done
- [ ] Edit task
- [ ] Save / Load from file

## Current Status (Day 7)

- Advanced string formatting (f-strings, alignment, centering)
- Search tasks by keyword in title (case-insensitive)
- Much nicer console output (borders, alignment, symbols)
- More consistent user messages and prompts

## Current Status (Day 8)

- Heavy use of functions with parameters & return values
- Separation of concerns: UI, logic, data manipulation separated
- New feature: mark task as completed (done status)
- Helper functions: print_header, get_valid_priority, create_task, get_sorted_tasks
- Cleaner and more maintainable code structure
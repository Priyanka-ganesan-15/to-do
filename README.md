# To-Do List App

## Overview

The To-Do List App is a simple desktop application built using Python's Tkinter library. This application allows users to manage their tasks by adding, viewing, and deleting them. Each task can be assigned a priority level (High, Medium, or Low) and an optional due date.

## Features

- **Add Task:** Users can add a new task with a priority level and an optional due date.
- **Delete Task:** Users can delete a selected task from the list.
- **Priority Levels:** Tasks can be categorized as High, Medium, or Low priority.
- **Due Date:** Users can assign a due date to tasks in the format `YYYY-MM-DD`.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/todo-app.git
    cd todo-app
    ```

2. **Install Dependencies:**

    Ensure you have Python installed (version 3.6 or higher). You can download it from [python.org](https://www.python.org/downloads/).

    No additional Python packages are required for this application as it uses Tkinter, which is included with standard Python installations.

## Usage

1. **Run the Application:**

    Navigate to the directory containing the script and run:

    ```bash
    python todo_app.py
    ```

2. **Add a Task:**

    - Enter the task description in the input field.
    - Select the priority level from the dropdown menu.
    - (Optional) Enter the due date in the format `YYYY-MM-DD`.
    - Click the "Add Task" button to add the task to the list.

3. **Delete a Task:**

    - Select the task you want to delete from the list.
    - Click the "Delete Task" button to remove the selected task.

## File Structure

- `todo_app.py`: The main script containing the `TodoApp` class and the `main` function to run the application.

## Code Explanation

### TodoApp Class

- **Initialization (`__init__` method):**
  - Sets up the main window and application title.
  - Configures the styles for buttons, entry fields, and labels.
  - Creates and arranges the input frame, list frame, and their respective widgets (entry fields, buttons, labels, and listbox).

- **add_task Method:**
  - Retrieves task details from the input fields.
  - Validates the due date format (if provided).
  - Adds the task to the listbox and internal tasks list.
  - Clears the input fields after adding the task.

- **delete_task Method:**
  - Deletes the selected task from the listbox and internal tasks list.
  - Displays a warning if no task is selected.

### main Function

- Initializes the Tkinter root window.
- Creates an instance of the `TodoApp` class.
- Starts the Tkinter main loop.


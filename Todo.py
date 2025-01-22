import json
import os

class TodoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
    
    def save_tasks(self):
        """Save tasks to a file."""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        """Add a new task."""
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        """Remove a task."""
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()

    def update_task(self, old_task, new_task):
        """Update a task."""
        if old_task in self.tasks:
            self.tasks[self.tasks.index(old_task)] = new_task
            self.save_tasks()

    def display_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks found.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

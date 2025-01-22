import unittest
from Todo import TodoApp

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of TodoApp before each test."""
        self.todo = TodoApp('test_tasks.json')

    def test_add_task(self):
        """Test adding a task."""
        self.todo.add_task("Finish homework")
        self.assertIn("Finish homework", self.todo.tasks)

    def test_remove_task(self):
        """Test removing a task."""
        self.todo.add_task("Finish homework")
        self.todo.remove_task("Finish homework")
        self.assertNotIn("Finish homework", self.todo.tasks)

    def test_update_task(self):
        """Test updating a task."""
        self.todo.add_task("Finish homework")
        self.todo.update_task("Finish homework", "Complete homework")
        self.assertIn("Complete homework", self.todo.tasks)
        self.assertNotIn("Finish homework", self.todo.tasks)

    def test_display_tasks(self):
        """Test displaying tasks."""
        self.todo.add_task("Finish homework")
        self.todo.add_task("Clean room")
        with self.assertLogs(self.todo.display_tasks(), level="INFO"):
            self.todo.display_tasks()

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists('test_tasks.json'):
            os.remove('test_tasks.json')

if __name__ == '__main__':
    unittest.main()

import unittest
from app import app, todos

class TodoApiTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self._reset_database()

    def _reset_database(self):
        # Directly modify the global todos list
        global todos
        todos.clear()  # Clear the list

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_add_todo_success(self):
        response = self.app.post('/todos', json={'todo': 'Test Task'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Todo added!')
        self.assertEqual(response.json['todo']['task'], 'Test Task')

    def test_add_todo_bad_request(self):
        response = self.app.post('/todos', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing "todo" field', response.json['message'])

if __name__ == '__main__':
    unittest.main()

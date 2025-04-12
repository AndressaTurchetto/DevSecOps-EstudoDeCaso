import unittest
from todo_project.todo_project import app


class TestBasic(unittest.TestCase):
    def test_home_status(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

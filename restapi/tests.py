from django.test import TestCase
from . models import Todo

# Create your tests here.

class TestCaseTodo(TestCase):
    def testTodo(self):
        todo = Todo(title="create django app", task="This is a django application")
        self.assertEqual(todo.title, "create django app")
        self.assertEqual(todo.task, "This is a django application")

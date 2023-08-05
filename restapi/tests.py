from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo  # Replace 'myapp' with the actual app name

class TodoModelTest(TestCase):
    def setUp(self):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='testuser', password='testpassword')
        Todo.objects.create(title='Test Todo', task='This is a test task.', owner=user)

    # def test_title_max_length(self):
    #     todo = Todo.objects.get(id=1)
    #     max_length = todo._meta.get_field('title').max_length
    #     self.assertEquals(max_length, 50)

    # def test_task_content(self):
    #     todo = Todo.objects.get(id=1)
    #     task = todo.task
    #     self.assertEquals(task, 'This is a test task.')

    def test_owner_relationship(self):
        todo = Todo.objects.get(id=1)
        owner = todo.owner
        self.assertTrue(isinstance(owner, User))
        self.assertEquals(owner.username, 'testuser')

    def test_todo_creation(self):
        todo_count = Todo.objects.count()
        self.assertEquals(todo_count, 1)

    # def test_todo_str_representation(self):
    #     todo = Todo.objects.get(id=1)
    #     self.assertEquals(str(todo), 'Test Todo')
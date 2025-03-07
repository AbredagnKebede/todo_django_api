from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "My Todo",
            body = "A body Todo"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "My Todo")
        self.assertEqual(self.todo.body, "A body Todo")
        self.assertEqual(str(self.todo), "My Todo")
        
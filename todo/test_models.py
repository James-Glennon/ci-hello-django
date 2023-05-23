from django.test import TestCase
from .models import Item
# Create your tests here.


class test_models(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

from django.test import TestCase
from .models import User

# Create your tests here.
class ModelTests(TestCase):
    
    def test_User_model(self):
        name = User.objects.create(name="elvis", surname="sebatane")
        self.assertEqual(str(name), "elvis", "names are not equal")
        self.assertEqual(str(name.surname), "sebatane", "surnames are not equal")
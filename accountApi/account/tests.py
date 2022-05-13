from django.test import TestCase
from .models import Account
from user.models import User

# Create your tests here.
class ModelTests(TestCase):
    def setUp(self):
        User.objects.create(name="sue", surname="veton")

    def test_User_model(self):
        user = User.objects.get(name="sue")
        account = Account.objects.create(user=user, type="SAVINGS", amount=5000.00)
        self.assertEqual(str(account.type), "SAVINGS", "account type not the same")
        self.assertEqual(account.amount, 5000.00, "account amount not equal")
        self.assertEqual(account.user, user, "account user does not exist")
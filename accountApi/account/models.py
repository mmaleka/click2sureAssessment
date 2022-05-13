from django.db import models
# from user.models import User
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):

    def __str__(self):
        return str(self.id)

    id = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    TYPE_CHOICES = (
        ('S', 'Savings'),
        ('C', 'Credit'),
    )
    type = models.CharField(max_length=10, default=None, choices=TYPE_CHOICES)
    amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    

'''Bank account to be one of either SAVINGS, or CREDIT
i. CREDIT account can have negative values up to a limit of R20,000.00.
ii. SAVINGS account to always have a positive value of R50.00 or more.'''
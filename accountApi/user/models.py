from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        name = self.user.first_name
        return name

    @property
    def surname(self):
        surname = self.user.last_name
        return surname

    def __str__(self):
        return self.name


# class User(models.Model):

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
#     id = models.IntegerField(primary_key=True, unique=True)
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
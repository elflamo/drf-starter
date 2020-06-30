from django.db import models
from django.contrib.auth.models import AbstractUser


class CreatedModified(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.username) + " | " + str(self.mobile)

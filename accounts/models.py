from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

# null=True can store a database entry of no value
# blank=True allows an empty value in a form to be valid
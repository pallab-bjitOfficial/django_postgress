"""
This module defines the database models for the application.

Models:
    User: Represents a user with a name and age.
"""

from django.db import models


class User(models.Model):
    """
    Represents a user in the system.

    Attributes:
        name (str): The name of the user.
        age (int): The age of the user.
    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return str(self.name)

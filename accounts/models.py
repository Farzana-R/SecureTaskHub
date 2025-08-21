from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This allows for additional fields and methods specific to the application.
    """
    # Add any additional fields here if needed
    class Roles(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        MANAGER = 'Manager', 'Manager'
        EMPLOYEE = 'Employee', 'Employee'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.EMPLOYEE,
        help_text="Role of the user in the system"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"

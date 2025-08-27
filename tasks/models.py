"""Models for the Task Management application."""
import os
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = [".pdf", ".dox"]
    if ext not in valid_extensions:
        raise ValidationError("Only PDF and DOCX files are allowed")
    

def valid_file_size(value):
    limit = 2 * 1024 * 1024 # 2 MB
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 2 MB")


# def task_upload_path(instance, filename):
#       TODO
#     return f"tasks/{instance.created_by.username}/{filename}"


class Task(models.Model):
    """Model representing a task in the task management application."""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    attachment = models.FileField(
        upload_to="task_file/",
        validators=[validate_file_extension, valid_file_size],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title} - {self.status}"

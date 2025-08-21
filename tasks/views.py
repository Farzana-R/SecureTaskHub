"""
This module contains views for task management, specifically for creating tasks.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import manager_required


@login_required
@manager_required
def create_task(request):
    """
    View to create a new task, accessible only by managers.
    """
    if request.method == 'POST':
        # Handle task creation logic here
        pass
    return render(request, 'tasks/create_task.html')
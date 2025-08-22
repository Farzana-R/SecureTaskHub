"""
This module contains views for task management, specifically for creating tasks.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import manager_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
@manager_required
def create_task(request):
    """
    View to create a new task, accessible only by managers.
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def task_list(request):
    """
    Admin can see all tasks,
    Managers can see tasks they created,
    Employees can see tasks assigned to them.
    """
    if request.user.role == 'ADMIN':
        # Fetch all tasks for admin
        tasks = Task.objects.all()
    elif request.user.role == 'MANAGER':
        # Fetch tasks created by the manager
        tasks = Task.objects.filter(created_by=request.user)
    elif request.user.role == 'EMPLOYEE':
        tasks = Task.objects.filter(assignee=request.user)
    else:
        tasks = Task.objects.none()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def update_task(request, pk):
    """
    View to update an existing task.
    Admin can update any task,
    Managers can update tasks they created,
    Employees can update tasks assigned to them.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return redirect('task_list')

    if request.user.role == 'ADMIN' or \
       (request.user.role == 'MANAGER' and task.created_by == request.user) or \
       (request.user.role == 'EMPLOYEE' and task.assignee == request.user):
        
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TaskForm(instance=task)
        return render(request, 'tasks/update_task.html', {'form': form, 'task': task})
    else:
        return redirect('task_list')
    

@login_required
@manager_required
def delete_task(request, pk):
    """
    View to delete an existing task.
    Admin can delete any task,
    Managers can delete tasks they created,
    Employees can delete tasks assigned to them.
    """
    try:
        # task = Task.objects.get(pk=pk)
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')
    except Task.DoesNotExist:
        return redirect('task_list')

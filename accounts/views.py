"""
This module contains views for user authentication and dashboard.
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Team, User
from .forms import RegisterForm, TeamForm
from .decorators import manager_required


def index(request):
    return render(request, "index.html")

# @login_required
# def dashboard(request):
#     """
#     Render the user dashboard.
#     """
#     user = request.user
#     return render(request, 'accounts/dashboard.html', {'user': user})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@manager_required
@login_required
def team_list(request):
    teams = Team.objects.all().prefetch_related("user_set") #optimized
    return render(request, 'accounts/team_list.html', {'teams': teams})


@login_required
@manager_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
        
    else:
        form = TeamForm()

    return render(request, 'accounts/team_form.html', {'form': form})


@login_required
@manager_required
def update_team(request, pk):
    pass
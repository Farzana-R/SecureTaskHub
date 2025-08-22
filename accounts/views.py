"""
This module contains views for user authentication and dashboard.
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm


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
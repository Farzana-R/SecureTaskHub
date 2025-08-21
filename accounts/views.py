"""
This module contains views for user authentication and dashboard.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import User

@login_required
def dashboard(request):
    """
    Render the user dashboard.
    """
    user = request.user
    return render(request, 'accounts/dashboard.html', {'user': user})

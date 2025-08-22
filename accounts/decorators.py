from django.core.exceptions import PermissionDenied


def admin_required(view_func):
    """
    Decorator to ensure that the user is an admin.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'ADMIN':
            raise PermissionDenied(
                "You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def manager_required(view_func):
    """
    Decorator to ensure that the user is a manager.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role not in ['Admin', 'Manager']:
            raise PermissionDenied(
                "You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def employee_required(view_func):
    """
    Decorator to ensure that the user is an employee.
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role not in ['ADMIN', 'MANAGER', 'EMPLOYEE']:
            raise PermissionDenied(
                "You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)

    return _wrapped_view

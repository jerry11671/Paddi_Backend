from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """Allows access to only admin"""

    def has_permission(self, request, view):
        # Check if the user is an Admin
        return request.user and request.user.is_superuser


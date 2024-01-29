from rest_framework import permissions

class IsActiveEmployeePermission(permissions.BasePermission):

    def has_permission(self, request, view):

        """Права доступа только для активных сотрудников"""

        return request.user.is_authenticated and request.user.is_active and request.user.is_staff

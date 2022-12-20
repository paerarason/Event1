from  rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import permissions
class IsCoordinator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Coordinator").exists()
            
class IsHeadCoordinator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="HEADCORDINATOR").exists()
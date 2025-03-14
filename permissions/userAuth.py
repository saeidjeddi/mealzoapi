from rest_framework.permissions import BasePermission

class Member(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.active or request.user.superuser:
                return True
            else:
                return False
        else:
            return False



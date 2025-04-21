from rest_framework.permissions import BasePermission

class GenrePermission(BasePermission):

    def has_permission(self, request, view):
        return False

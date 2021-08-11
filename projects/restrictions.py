from rest_framework.permissions import BasePermission


class IsFullAdmin(BasePermission):
    """
    Allows access only to authenticated profiles.
    """

    def has_permission(self, request, view):
        return bool()

from rest_framework import permissions

from users.models import User


class IsCreatorOrAdminOrModerator(permissions.BasePermission):

    message = "Changing available only for creators or admins"

    def has_object_permission(self, request, view, obj):

        if request.user.role == User.MODERATOR or request.user.role == User.ADMIN:
            return True

        if obj.author == request.user:
            return True

        return False

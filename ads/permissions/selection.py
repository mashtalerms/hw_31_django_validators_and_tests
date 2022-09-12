from rest_framework import permissions


class IsCreator(permissions.BasePermission):

    message = "Changing available only for creators"

    def has_object_permission(self, request, view, obj):

        if obj.owner == request.user:
            return True

        return False

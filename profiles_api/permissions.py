from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj): #attempted object that we want to make changes on
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:#GET is safe method
            return True

        return obj.id == request.user.id #object they are updating matches their own id

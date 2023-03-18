from rest_framework import permissions

""" !!!!!!!!!!!!!!!!!
has_object_permission is never executed for list views (regardless of the view you're extending from) or
when the request method is POST (since the object doesn't exist yet).
https://testdriven.io/blog/drf-permissions/
!!!!!!!!!!!!!!!!"""
# from articles.models import Article
#
# class IsAuthorPermission(permissions.BasePermission):
#
#
#     def has_permission(self, request, view):
#         qs = Article.objects.filter(author=request.user)
#         return qs.exists()


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        # # Read permissions are allowed to any request,
        # # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # All permissions are only allowed to the owner of the note.
        return obj.author_id == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or Admin to access it.
    """

    def has_object_permission(self, request, view, obj):
        # # Read permissions are allowed to any request,
        # # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        # All permissions are only allowed to the owner of the note or Admin.
        return bool(request.user and request.user.is_superuser) or (
            obj.user == request.user
        )

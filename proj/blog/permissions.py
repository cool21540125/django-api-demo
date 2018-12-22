from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):    # 擁有者才能改
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS = [GET, HEAD, OPTIONS]
            return True

        return obj.owner == request.user
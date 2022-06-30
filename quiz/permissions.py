from rest_framework import permissions

class StafCUDAuthenticatedOnlyRead(permissions.IsAdminUser):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated:
            return True
        elif request.method in ('POST', 'PUT', 'PATCH', 'DELETE') and request.user and request.user.is_staff:
            return True
        else:
            return False

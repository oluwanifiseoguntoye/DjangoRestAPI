# by using a mixin, i'm able to include the custom authorization
# in my views rather than reuse the same permission_class in my close

from .permissions import IsStaffEditorPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
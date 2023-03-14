from django.urls import include, path, re_path

from .invitations import urls as invitation_urls
from .users import urls as user_urls
from .views import (
    WorkspaceLeaveView,
    WorkspaceOrderView,
    WorkspacePermissionsView,
    WorkspacesView,
    WorkspaceView,
)

app_name = "baserow.api.workspaces"

urlpatterns = [
    path("users/", include(user_urls, namespace="users")),
    path("invitations/", include(invitation_urls, namespace="invitations")),
    re_path(r"^$", WorkspacesView.as_view(), name="list"),
    re_path(
        r"(?P<workspace_id>[0-9]+)/permissions/$",
        WorkspacePermissionsView.as_view(),
        name="permissions",
    ),
    re_path(
        r"(?P<workspace_id>[0-9]+)/leave/$", WorkspaceLeaveView.as_view(), name="leave"
    ),
    re_path(r"(?P<workspace_id>[0-9]+)/$", WorkspaceView.as_view(), name="item"),
    re_path(r"order/$", WorkspaceOrderView.as_view(), name="order"),
]

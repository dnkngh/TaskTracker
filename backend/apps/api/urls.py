from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views import (
    ProjectViewSet,
    ProjectPermissionViewSet,
    ProjectTaskStatusViewSet,
    ProjectUserPermissionViewSet,
    TaskViewSet,
    TaskAssigneeViewSet,
    TaskLogTimeViewSet,
    UserViewSet
)

app_name = 'api'

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('projectpermission', ProjectPermissionViewSet)
router.register('projecttaskstatus', ProjectTaskStatusViewSet)
router.register('projectuserpermission', ProjectUserPermissionViewSet)
router.register('tasks', TaskViewSet)
router.register('taskassignee', TaskAssigneeViewSet)
router.register('tasklogtimes', TaskLogTimeViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

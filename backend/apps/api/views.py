from django.contrib.auth import get_user_model
from rest_framework import viewsets

from apps.api.serializers import (
    ProjectSerializer,
    ProjectPermissionSerializer,
    ProjectTaskStatusSerializer,
    ProjectUserPermissionSerializer,
    TaskSerializer,
    TaskAssigneeSerializer,
    TaskLogTimeSerializer,
    UserSerializer
)
from apps.projects.models import (
    Project,
    ProjectPermission,
    ProjectTaskStatus,
    ProjectUserPermission
)
from apps.tasks.models import Task, TaskAssignee, TaskLogTime

User = get_user_model()


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectPermissionViewSet(viewsets.ModelViewSet):
    queryset = ProjectPermission.objects.all()
    serializer_class = ProjectPermissionSerializer


class ProjectTaskStatusViewSet(viewsets.ModelViewSet):
    queryset = ProjectTaskStatus.objects.all()
    serializer_class = ProjectTaskStatusSerializer


class ProjectUserPermissionViewSet(viewsets.ModelViewSet):
    queryset = ProjectUserPermission.objects.all()
    serializer_class = ProjectUserPermissionSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskAssigneeViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignee.objects.all()
    serializer_class = TaskAssigneeSerializer


class TaskLogTimeViewSet(viewsets.ModelViewSet):
    queryset = TaskLogTime.objects.all()
    serializer_class = TaskLogTimeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

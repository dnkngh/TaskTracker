from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.serializers import (
    ProjectSerializer,
    TaskSerializer,
    TaskLogTimeSerializer,
    UserSerializer
)
from tasks.models import Project, Task, TaskLogTime

User = get_user_model()


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskLogTimeViewSet(viewsets.ModelViewSet):
    queryset = TaskLogTime.objects.all()
    serializer_class = TaskLogTimeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.projects.models import (
    Project,
    ProjectPermission,
    ProjectTaskStatus,
    ProjectUserPermission
)
from apps.tasks.models import Task, TaskAssignee, TaskLogTime

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPermission
        fields = '__all__'


class ProjectTaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTaskStatus
        fields = '__all__'


class ProjectUserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUserPermission
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignee
        fields = '__all__'


class TaskLogTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLogTime
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.projects.models import Project
from apps.tasks.models import Task, TaskLogTime

User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskLogTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskLogTime
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

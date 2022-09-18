from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, TaskViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views import (
    ProjectViewSet,
    TaskViewSet,
    TaskLogTimeViewSet,
    UserViewSet
)

app_name = 'api'

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('tasklogtimes', TaskLogTimeViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

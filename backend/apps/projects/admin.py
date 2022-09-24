from django.contrib import admin

from apps.projects.models import (
    Project,
    ProjectPermission,
    ProjectTaskStatus,
    ProjectUserPermission
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'code',
        'creator',
        'owner',
        'description',
    )


@admin.register(ProjectTaskStatus)
class ProjectTaskStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order_number',
        'name',
        'project',
    )


@admin.register(ProjectPermission)
class ProjectPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'project',
        'permission',
    )


@admin.register(ProjectUserPermission)
class ProjectUserPermissionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'project',
        'user',
        'permission',
    )

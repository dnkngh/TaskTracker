from django.contrib import admin

from apps.projects.models import Project, ProjectTaskStatus


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'code',
        'creator',
        'description',
    )


@admin.register(ProjectTaskStatus)
class ProjectTaskStatusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

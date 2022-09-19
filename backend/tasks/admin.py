from django.contrib import admin

from tasks.models import Project, ProjectTaskStatus, Task, TaskLogTime


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


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'project',
        'priority',
        'status',
        'creator',
        'executor',
        'text',
        'pub_date',
        'deadline',
    )


@admin.register(TaskLogTime)
class TaskLogTimeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'task',
        'time_spent',
        'comment',
        'log_date',
    )

from django.contrib import admin

from tasks.models import Project, Task, TaskLoggedTime


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'code',
        'creator',
        'description',
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'project',
        'creator',
        'executor',
        'text',
        'pub_date',
        'deadline',
    )


@admin.register(TaskLoggedTime)
class TaskLoggedTimeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'task',
        'time_spent',
        'comment',
        'log_date',
    )

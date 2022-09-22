from django.contrib import admin

from apps.tasks.models import Task, TaskAssignee, TaskLogTime


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'project',
        'priority',
        'status',
        'creator',
        'text',
        'pub_date',
        'deadline',
    )


@admin.register(TaskAssignee)
class TaskAssigneeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'task',
        'assignee',
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

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='project name',
        help_text='project name',
    )
    code = models.CharField(
        max_length=10,
        verbose_name='project code',
        help_text='project code',
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='project description',
        help_text='project description',
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_projects',
        verbose_name='project creator',
        help_text='project creator',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='owned_projects',
        verbose_name='project owner',
        help_text='project owner',
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class ProjectTaskStatus(models.Model):
    name = models.CharField(
        max_length=15,
        verbose_name='status name',
        help_text='status name',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='task_statuses',
        verbose_name='related project',
        help_text='related project',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'ProjectTaskStatus'
        verbose_name_plural = 'ProjectTaskStatus'


class Task(models.Model):
    PRIORITY_OPTIONS = (
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    )
    STATUS_OPTIONS = (
        ('OPEN', 'OPEN'),
        ('TO DO', 'TO DO'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('DONE', 'DONE'),
    )
    name = models.CharField(
        max_length=100,
        verbose_name='task name',
        help_text='task name',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='related project',
        help_text='related project',
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_OPTIONS,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_tasks',
        verbose_name='task creator',
        help_text='task creator',
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='tasks',
        verbose_name='task executor',
        help_text='task executor',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='date created',
        help_text='date created',
    )
    status = models.ForeignKey(
        ProjectTaskStatus,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='task status',
        help_text='task status',
        blank=True,
        null=True
    )
    deadline = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='task deadline',
        help_text='task deadline',
    )
    text = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='task description',
        help_text='task description',
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name


class TaskLogTime(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='logged_time',
        verbose_name='executor',
        help_text='executor',
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='logged_time',
        verbose_name='related task',
        help_text='related task',
    )
    time_spent = models.DurationField(
        db_index=True,
        verbose_name='time spent',
        help_text='time spent',
    )
    log_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='log date',
        help_text='log date',
    )
    comment = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='comment',
        help_text='comment',
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'TaskLogTime'
        verbose_name_plural = 'TaskLogTime'

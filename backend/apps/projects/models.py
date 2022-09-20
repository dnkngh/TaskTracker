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
        verbose_name_plural = 'Project'

    def __str__(self):
        return self.name


class ProjectTaskStatus(models.Model):
    """Модель статусов задач в проекте: ToDo, In progress ..."""
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
        ordering = ('project',)
        verbose_name = 'ProjectTaskStatus'
        verbose_name_plural = 'ProjectTaskStatus'


class ProjectPermission(models.Model):
    """Права доступа в проекте"""
    name = models.CharField(
        max_length=30,
        verbose_name='permission name',
        help_text='permission name',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='permissions',
        verbose_name='related project',
        help_text='related project',
    )
    can_view = models.BooleanField(
        null=False,
        verbose_name='view permission',
        help_text='view permission',
    )
    can_participate = models.BooleanField(
        null=False,
        verbose_name='participant permission',
        help_text='participant permission',
    )
    can_moderate = models.BooleanField(
        null=False,
        verbose_name='moderator permission',
        help_text='moderator permission',
    )

    def __str__(self):
        return f'{self.name} - {self.project.name}'

    class Meta:
        ordering = ('project',)
        verbose_name = 'ProjectPermission'
        verbose_name_plural = 'ProjectPermission'


class ProjectUserPermission(models.Model):
    """Права доступа конкретного пользователя в рамках проекта"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_user_permissions',
        verbose_name='related project',
        help_text='related project',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_project_permissions',
        verbose_name='related user',
        help_text='relater user',
    )
    permission = models.ForeignKey(
        ProjectPermission,
        on_delete=models.CASCADE,
        related_name='all_user_permissions',
        verbose_name='relater project permission',
        help_text='relater project permission',
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'ProjectUserPermission'
        verbose_name_plural = 'ProjectUserPermission'

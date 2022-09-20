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

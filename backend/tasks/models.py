from django.db import models

from users.models import User


class Task(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='task name',
        help_text='task name',
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
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

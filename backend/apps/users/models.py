from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='email',
        help_text='email',
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='first name',
        help_text='first name',
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='last name',
        help_text='last name',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ('id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

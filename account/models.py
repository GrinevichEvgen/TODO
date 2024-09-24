from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Добавляем related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Добавляем related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

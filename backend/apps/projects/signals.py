from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.projects.models import Project, ProjectPermission, ProjectUserPermission

User = get_user_model()


@receiver(post_save, sender=Project)
def create_project_permission(sender, instance, created, **kwargs):
    if created:
        permission = ProjectPermission.objects.create(
            name='Project administator',
            project=instance,
            permission='ADMINISTRATOR',
        )
        ProjectUserPermission.objects.create(
            project=instance,
            user=instance.creator,
            permission=permission,
        )

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.projects.models import Project, ProjectTaskStatus, ProjectPermission

from apps.core.management.data.projects import (
    PROJECTS,
    PROJECTS_TASK_STATUS,
    PROJECT_PERMISSIONS
)
from apps.core.management.data.users import USERS

User = get_user_model()


class Command(BaseCommand):
    help = 'creates default objects'

    def handle(self, *args, **options):
        """Создание объектов моделей"""
        # Users
        users_created = False
        if not User.objects.all():
            User.objects.bulk_create(
                User(
                    email=user.get('email'),
                    first_name=user.get('first_name'),
                    last_name=user.get('last_name'),
                    username=user.get('username'),
                    password=user.get('password')
                ) for user in USERS
            )
            users_created = True
            print(
                f'Users created: {", ".join([user["email"] for user in USERS])}'
            )
        else:
            print('USERS ALREADY EXIST')

        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                email='a@a.com',
                first_name='Bran',
                last_name='Stark',
                username='Third-Eyed Raven',
                password='admin',
            )
            print('Admin user a@a.com CREATED')
        else:
            print('ADMIN USER ALREADY EXISTS')

        if users_created:
            # Projects
            Project.objects.bulk_create(
                Project(
                    name=project.get('name'),
                    code=project.get('code'),
                    description=project.get('description')
                ) for project in PROJECTS
            )
            print(
                f'Projects created: {", ".join([project["name"] for project in PROJECTS])}'
            )

            for pr in PROJECTS:
                # ProjectTaskStatus
                project_obj = Project.objects.get(name=pr.get('name'))
                for task_status in PROJECTS_TASK_STATUS:
                    ProjectTaskStatus.objects.create(
                        name=task_status,
                        project=project_obj,
                    )
                # ProjectPermission
                ProjectPermission.objects.bulk_create(
                    ProjectPermission(
                        name=permission.get('name'),
                        project=project_obj,
                        can_view=permission.get('can_view'),
                        can_participate=permission.get('can_participate'),
                        can_moderate=permission.get('can_moderate'),
                    ) for permission in PROJECT_PERMISSIONS
                )
            print(
                f'ProjectTaskStatuses created: {", ".join(PROJECTS_TASK_STATUS)}'
            )
            print(
                f'ProjectPermissions created: {", ".join(permission.get("name") for permission in PROJECT_PERMISSIONS)}'
            )

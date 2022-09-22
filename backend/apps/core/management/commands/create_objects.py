from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.projects.models import Project, ProjectTaskStatus

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
                f'USERS {", ".join([user["email"] for user in USERS])} CREATED'
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
            print('ADMIN USER a@a.com CREATED')
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
                f'Projects {", ".join([project["name"] for project in PROJECTS])}'
            )

            # ProjectTaskStatus
            for pr in PROJECTS:
                project_obj = Project.objects.get(name=pr.get('name'))
                for task_status in PROJECTS_TASK_STATUS:
                    ProjectTaskStatus.objects.create(
                        name=task_status,
                        project=project_obj,
                    )
            print(
                f'ProjectTaskStatuses {", ".join(PROJECTS_TASK_STATUS)} CREATED'
            )

            # ProjectPermission


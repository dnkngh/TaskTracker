from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.db.models.aggregates import Sum

from apps.projects.models import Project

User = get_user_model()

EMPTY_VALUE_MESSAGE = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'get_projects',
        'get_total_time_spent',
        'is_staff',
    )

    @admin.display(description='projects')
    def get_projects(self, obj):

        perm = obj.project_permissions.values()

        print(perm)
        # return '\n'.join([project['permission'] for project in list_])


        list_ = obj.created_projects.values('name')
        return '\n'.join([project['name'] for project in list_])

    @admin.display(
        description='total time spent', empty_value=EMPTY_VALUE_MESSAGE
    )
    def get_total_time_spent(self, obj):
        return (
            obj.logged_time.values('time_spent').aggregate(
                total_time=Sum('time_spent')
            ).get('total_time')
        )

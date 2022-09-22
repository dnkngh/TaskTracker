from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


USERS = [
    {
        'email': 'john@stark.nord',
        'first_name': 'John',
        'last_name': 'Snow',
        'username': 'The Bastard of Winterfell',
        'password': '123qweASD',
    },
    {
        'email': 'eddard@stark.nord',
        'first_name': 'Eddard',
        'last_name': 'Stark',
        'username': 'Ned',
        'password': '123qweASD',
    },
    {
        'email': 'jamie@lannister.com',
        'first_name': 'Jamie',
        'last_name': 'Lannister',
        'username': 'The Kingslayer',
        'password': '123qweASD',
    },
    {
        'email': 'cersei@lannister.com',
        'first_name': 'Cersei',
        'last_name': 'Lannister',
        'username': 'The Bitch',
        'password': '123qweASD',
    },
    {
        'email': 'tyrion@lannister.com',
        'first_name': 'Tyrion',
        'last_name': 'Lannister',
        'username': 'The Halfman',
        'password': '123qweASD',
    },
]


class Command(BaseCommand):
    help = 'creates default objects'

    def handle(self, *args, **options):
        User.objects.bulk_create(
            User(
                email=user.get('email'),
                first_name=user.get('first_name'),
                last_name=user.get('last_name'),
                username=user.get('username'),
                password=user.get('password')
            ) for user in USERS
        )
        print(f'USERS {", ".join([user["email"] for user in USERS])} CREATED')



# [
#     User(
#         email='eddard@stark.nord',
#         first_name='Eddard',
#         second_name='Stark',
#         username='Ned',
#         password='123qwe#2B'
#     ),
#     User(email='john@stark.nord', first_name='John', second_name='Snow', username='The Bastard of Winterfell',
#          password='123qwe#2E'),
#     User(email='jamie@lannister.com', first_name='Jamie', second_name='Lannister', username='The Kingslayer',
#          password='123qwe#2C'),
#     User(email='cersei@lannister.com', first_name='Cersei', second_name='Lannister', username='Bitch',
#          password='123qwe#2D'),
#     User(email='tyrion@lannister.com', first_name='Tyrion', second_name='Lannister', username='The Halfman',
#          password='123qwe#2F'),
# ]
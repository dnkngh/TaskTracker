PROJECTS = [
    {
        'name': 'Winterfell',
        'code': 'WF',
        'description': 'Winter preparation roadmap',
        'creator': 'Eddard',
        'viewer': 'Varys',
    },
    {
        'name': 'Casterly Rock',
        'code': 'CR',
        'description': 'Wars swallow gold like a pit in the Earth',
        'creator': 'Tywin',
        'viewer': 'Varys',
    },
    {
        'name': 'Dragonstone',
        'code': 'DS',
        'description': 'Fire and Blood',
        'creator': 'Daenerys',
        'viewer': 'Varys',
    },
]

PROJECTS_TASK_STATUS = [
    {
        'order_number': 1,
        'name': 'Open'
     },
    {
        'order_number': 2,
        'name': 'To do'
     },
    {
        'order_number': 3,
        'name': 'In progress'
    },
    {
        'order_number': 4,
        'name': 'Done'
    },
    {
        'order_number': 5,
        'name': 'Closed'
    },
]

PROJECT_PERMISSIONS = [
    {
        'name': 'viewer',
        'permission': 'VIEWER',
    },
    {
        'name': 'user',
        'permission': 'PARTICIPANT',
    },
    {
        'name': 'lead',
        'permission': 'ADMINISTRATOR',
    },
]

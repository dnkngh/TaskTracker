PROJECTS = [
    {
        'name': 'Winterfell',
        'code': 'WF',
        'description': 'Winter preparation roadmap',
    },
    {
        'name': 'Casterly Rock',
        'code': 'CR',
        'description': 'Wars swallow golds like a pit in the Earth'
    }
]

PROJECTS_TASK_STATUS = [
    'Open',
    'To do',
    'In progress',
    'Done',
    'Closed',
]

PROJECT_PERMISSIONS = [
    {
        'name': 'viewer',
        'can_view': True,
        'can_participate': False,
        'can_moderate': False,
    },
    {
        'name': 'user',
        'can_view': True,
        'can_participate': True,
        'can_moderate': False,
    },
    {
        'name': 'lead',
        'can_view': True,
        'can_participate': True,
        'can_moderate': True,
    },
]

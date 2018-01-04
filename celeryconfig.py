from datetime import timedelta

BROKER_URL = 'redis://localhost:6379/0'

# Logging
CELERYD_TASK_LOG_FORMAT = 'info'
CELERY_REDIRECT_STDOUTS = True
CELERY_REDIRECT_STDOUTS_LEVEL = 'INFO'
CELERYD_LOG_COLOR = False

# Serialization
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

# Clock
CELERY_TIMEZONE = 'America/Santiago'
CELERY_ENABLE_UTC = False

# Pool
CELERYD_CONCURRENCY = 6

# Scheduler
CELERYBEAT_SCHEDULE = {
    'test-every-10-seconds': {
        'task': 'tasks.test',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
}

CELERY_ROUTES = {'tasks.test': {'queue': 'firstq'}}

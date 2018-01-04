from celery import Celery
from decorators import lock_on_task_error, LoginError
import random

app = Celery()
app.config_from_object('celeryconfig')

@app.task(bind=True, ignore_result=True)
@lock_on_task_error(60)
def test(self, banco='chile', rut='160987928',
         passwd_hash='fbc71ce36cc20790f2eeed2197898e71'):
    if random.random() >= 0.5:
        raise LoginError
    else:
        print("Get data")
        return True

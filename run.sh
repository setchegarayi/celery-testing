#!/bin/bash
if [ $APPLICATION_TYPE = "api" ] ; then
    gunicorn api:app --log-file=- --reload -b 0.0.0.0:8000

elif [ $APPLICATION_TYPE = "workers" ] ; then
    for run in {1..2}
    do
      celery worker -A tasks --loglevel=info -Q $ENV.scheduled -P solo &
      celery worker -A tasks --loglevel=info -Q $ENV.priority -P solo &
      celery worker -A tasks --loglevel=info -Q $ENV.regular -P solo &
    done
    tail -f /dev/null

elif [ $APPLICATION_TYPE = "scheduled" ] ; then
    rm celerybeat.pid 2> /dev/null
    for run in {1..4}
    do
      celery worker -A tasks --loglevel=info -Q $ENV.scheduled -P solo &
    done
    celery -A tasks beat --loglevel=info

elif [ "workers" = "workers" ] ; then
    for run in {1..4}
    do
      celery worker -A tasks --loglevel=info -P solo &
    done
    tail -f /dev/null
fi

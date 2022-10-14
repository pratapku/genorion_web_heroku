release: python manage.py migrate
web: daphne myproject.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A myproject.celery worker -l info
celerybeat: celery -A myproject beat -l INFO 
celeryworker2: celery -A myproject.celery worker & celery -A myproject beat -l INFO & wait -n
##

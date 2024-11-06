from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'predictor.settings')

app = Celery('predictor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'envoyer_rappel_rdv': {
        'task': 'diabete_predict.tasks.envoyer_rappel_rdv',
        'schedule': crontab(minute='*'),
    },
    'envoyer_rappel_rdv_aujourdhui': {
        'task': 'diabete_predict.tasks.envoyer_rappel_rdv_aujourdhui',
        'schedule': crontab(minute='*'),
    },
}

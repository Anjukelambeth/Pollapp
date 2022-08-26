from celery.schedules import crontab
from celery import periodic_task
from django.utils import timezone
from .models import Poll
import datetime
@periodic_task(run_every=crontab(minute='*/5'))
def delete_old_foos():
    d = timezone.now() - datetime.timedelta(hours=24)
    poll = Poll.objects.filter(timestamp__lt=d)
    poll.delete()
        # log deletion
    
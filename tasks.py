from celery import Celery
from apps.badges.constants import PIONNEER_TASK_BEAT

app = Celery('tasks', broker='redis://localhost')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(PIONNEER_TASK_BEAT, check_pioneer_badge.s(), name='check pionneer badge')


@app.task
def check_pioneer_badge():
    from accounts.models import Profile
    from badges.validator import BadgeValidator

    for profile in Profile.objects.filter_pionneers():
        BadgeValidator.grant_pionneer_badge(profile)

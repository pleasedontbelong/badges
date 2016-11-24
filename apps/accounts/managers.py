from django.utils import timezone
from django.db import models
from badges.constants import TIMEDELTA_FOR_PIONNEER


class ProfilesManager(models.Manager):
    def filter_pionneers(self):
        return self.filter(user__date_joined__lte=timezone.now() - TIMEDELTA_FOR_PIONNEER)

from django.utils import timezone
from userena.managers import UserenaBaseProfileManager
from badges.constants import TIMEDELTA_FOR_PIONNEER


class ProfilesManager(UserenaBaseProfileManager):
    def filter_pionneers(self):
        return self.filter(user__date_joined__lte=timezone.now() - TIMEDELTA_FOR_PIONNEER)

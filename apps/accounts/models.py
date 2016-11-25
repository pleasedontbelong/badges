from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from badges.constants import BADGES
from django.db import models
from .managers import ProfilesManager


class Profile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
    nb_views = models.IntegerField(default=0)

    objects = ProfilesManager()

    def increment_nb_views(self):
        self.nb_views += 1
        self.save(update_fields=('nb_views',))

    def has_star_badge(self):
        return self.badges.filter(identifier=BADGES.STAR).exists()

    def has_collector_badge(self):
        return self.badges.filter(identifier=BADGES.COLLECTOR).exists()

    def has_pionneer_badge(self):
        return self.badges.filter(identifier=BADGES.PIONNEER).exists()

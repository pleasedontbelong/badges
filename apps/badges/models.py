from __future__ import unicode_literals

from django.db import models
from .constants import BADGES


class Badge(models.Model):
    achievers = models.ManyToManyField('accounts.Profile', related_name="badges")
    identifier = models.PositiveIntegerField(unique=True, choices=BADGES, default=BADGES.STAR)

    def __unicode__(self):
        return BADGES.for_value(self.identifier).display

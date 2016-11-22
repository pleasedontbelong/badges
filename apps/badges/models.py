from __future__ import unicode_literals

from django.db import models


class Badge(models.Model):
    name = models.CharField(max_length=250)
    achievers = models.ManyToManyField('accounts.Profile', related_name="badges")

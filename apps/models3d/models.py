from __future__ import unicode_literals

from django.db import models


class Model3D(models.Model):
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=250, blank=False, null=True)

    def __unicode__(self):
        return self.name

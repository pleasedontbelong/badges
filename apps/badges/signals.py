from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from accounts.models import Profile
from models3d.models import Model3D
from .validator import BadgeValidator


@receiver(post_save, sender=Profile)
def check_star_badge(sender, **kwargs):
    if BadgeValidator.check_star_badge(kwargs['instance']):
        BadgeValidator.grant_star_badge(kwargs['instance'])


@receiver(post_save, sender=Model3D)
def check_collector_badge(sender, **kwargs):
    if kwargs['created'] and BadgeValidator.check_collector_badge(kwargs['instance'].profile):
        BadgeValidator.grant_collector_badge(kwargs['instance'].profile)

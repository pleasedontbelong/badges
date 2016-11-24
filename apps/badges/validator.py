from django.utils import timezone
from .models import Badge
from .constants import (NB_VIEWS_FOR_STAR, NB_MODELS_FOR_COLLECTOR,
                        TIMEDELTA_FOR_PIONNEER, BADGES)


class BadgeValidator(object):

    @staticmethod
    def check_star_badge(profile):
        return profile.nb_views >= NB_VIEWS_FOR_STAR

    @staticmethod
    def check_collector_badge(profile):
        return profile.model3d_set.count() >= NB_MODELS_FOR_COLLECTOR

    @staticmethod
    def check_pionneer_badge(profile):
        return profile.user.date_joined <= timezone.now() - TIMEDELTA_FOR_PIONNEER

    @staticmethod
    def grant_star_badge(profile):
        profile.badges.add(Badge.objects.get(identifier=BADGES.STAR))

    @staticmethod
    def grant_collector_badge(profile):
        profile.badges.add(Badge.objects.get(identifier=BADGES.COLLECTOR))

    @staticmethod
    def grant_pionneer_badge(profile):
        profile.badges.add(Badge.objects.get(identifier=BADGES.PIONNEER))

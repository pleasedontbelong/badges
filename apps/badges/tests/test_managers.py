from datetime import timedelta
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import Profile
from models3d.models import Model3D
from badges.constants import NB_VIEWS_FOR_STAR, TIMEDELTA_FOR_PIONNEER
from badges.validator import BadgeValidator
from mock import patch

User = get_user_model()


class ManagerTests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="john",
            email="john@beatles.com",
            password="john123")
        self.profile = Profile.objects.create(user=user)

    def test_check_star_badge(self):
        self.profile.nb_views = NB_VIEWS_FOR_STAR + 1
        self.profile.save()
        self.assertTrue(BadgeValidator.check_star_badge(self.profile))

    def test_check_star_badge_ko(self):
        self.profile.nb_views = NB_VIEWS_FOR_STAR - 1
        self.profile.save()
        self.assertFalse(BadgeValidator.check_star_badge(self.profile))

    @patch('badges.validator.NB_MODELS_FOR_COLLECTOR', 1)
    def test_check_collector_badge(self):
        Model3D.objects.create(profile=self.profile)
        self.assertTrue(BadgeValidator.check_collector_badge(self.profile))

    @patch('badges.validator.NB_MODELS_FOR_COLLECTOR', 1)
    def test_check_collector_badge_ko(self):
        self.assertFalse(BadgeValidator.check_collector_badge(self.profile))

    def test_check_pionneer_badge(self):
        self.profile.user.date_joined = timezone.now() - TIMEDELTA_FOR_PIONNEER - timedelta(seconds=1)
        self.profile.user.save()
        self.assertTrue(BadgeValidator.check_pionneer_badge(self.profile))

    def test_check_pionneer_badge_ko(self):
        self.profile.user.date_joined = timezone.now()
        self.profile.user.save()
        self.assertFalse(BadgeValidator.check_pionneer_badge(self.profile))

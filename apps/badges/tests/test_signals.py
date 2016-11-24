from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Profile
from models3d.models import Model3D
from badges.constants import NB_VIEWS_FOR_STAR
from mock import patch

User = get_user_model()


class ValidatorTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="john",
            email="john@beatles.com",
            password="john123")
        self.profile = Profile.objects.create(user=user)

    def test_check_star_badge(self):
        self.profile.nb_views = NB_VIEWS_FOR_STAR + 1
        self.profile.save()
        self.assertTrue(self.profile.has_star_badge())

    @patch('badges.validator.NB_MODELS_FOR_COLLECTOR', 1)
    def test_check_collector_badge(self):
        Model3D.objects.create(profile=self.profile)
        self.assertTrue(self.profile.has_collector_badge())

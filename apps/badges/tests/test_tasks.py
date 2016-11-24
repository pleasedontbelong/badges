from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Profile
from badges.constants import TIMEDELTA_FOR_PIONNEER
from tasks import check_pioneer_badge

User = get_user_model()


class TasksTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="john",
            email="john@beatles.com",
            password="john123")
        self.profile = Profile.objects.create(user=user)

    def test_pionneer_task(self):
        self.profile.user.date_joined = timezone.now() - TIMEDELTA_FOR_PIONNEER - timedelta(seconds=1)
        self.profile.user.save()
        check_pioneer_badge()
        self.assertTrue(self.profile.has_pionneer_badge())

    def test_pionneer_task_ko(self):
        self.profile.user.date_joined = timezone.now() - TIMEDELTA_FOR_PIONNEER + timedelta(seconds=1)
        self.profile.user.save()
        check_pioneer_badge()
        self.assertFalse(self.profile.has_pionneer_badge())

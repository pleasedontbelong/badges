from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from accounts.models import Profile
User = get_user_model()


class ProfileDetailViewsTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="john",
            email="john@beatles.com",
            password="john123")
        self.profile = Profile.objects.create(user=user)

    def test_incremented_view_online(self):
        self.client.force_login(self.profile.user, backend=settings.AUTHENTICATION_BACKENDS[0])
        old_nb_views = self.profile.nb_views
        response = self.client.get(reverse('profile_detail', kwargs={"username": self.profile.user.username}))
        self.assertEqual(response.status_code, 200)

        self.profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(self.profile.nb_views, old_nb_views + 1)

    def test_incremented_view_offline(self):
        old_nb_views = self.profile.nb_views
        response = self.client.get(reverse('profile_detail', kwargs={"username": self.profile.user.username}))
        self.assertEqual(response.status_code, 200)

        self.profile = Profile.objects.get(pk=self.profile.pk)
        self.assertEqual(self.profile.nb_views, old_nb_views + 1)

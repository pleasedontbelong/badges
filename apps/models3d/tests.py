from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings
from accounts.models import Profile
User = get_user_model()


class Model3DViewsTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="john",
            email="john@beatles.com",
            password="john123")
        self.profile = Profile.objects.create(user=user)

    def test_access(self):
        self.client.force_login(self.profile.user, backend=settings.AUTHENTICATION_BACKENDS[0])
        response = self.client.get(reverse('model_3d_create', kwargs={"username": self.profile.user.username}))
        self.assertEqual(response.status_code, 200)

    def test_access_ko(self):
        response = self.client.get(reverse('model_3d_create', kwargs={"username": self.profile.user.username}))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('userena_signin'), response['location'])

    def test_assigned_connected_user(self):
        self.client.force_login(self.profile.user, backend=settings.AUTHENTICATION_BACKENDS[0])
        data = {"name": "test model"}
        self.assertEqual(self.profile.model3d_set.count(), 0)
        response = self.client.post(
            reverse(
                'model_3d_create',
                kwargs={"username": self.profile.user.username}
            ),
            data
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.profile.model3d_set.count(), 1)

    def test_assigned_disconnected_user(self):
        data = {"name": "test model"}
        self.assertEqual(self.profile.model3d_set.count(), 0)
        response = self.client.post(
            reverse(
                'model_3d_create',
                kwargs={"username": self.profile.user.username}
            ),
            data
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('userena_signin'), response['location'])
        self.assertEqual(self.profile.model3d_set.count(), 0)

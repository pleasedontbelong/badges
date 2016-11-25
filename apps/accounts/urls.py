from django.conf.urls import url, include
from .views import ProfileDetailView


urlpatterns = [
    url(r'^accounts/(?P<username>(?!(signout|signup|signin)/)[\@\.\w-]+)/$',
        ProfileDetailView.as_view(),
        name='profile_detail'),
    url(r'^accounts/', include('userena.urls')),
]

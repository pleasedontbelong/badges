from django.conf.urls import url
from .views import Model3DCreateView


urlpatterns = [
    url(r'^(?P<username>[\@\.\w-]+)/models/add$',
        Model3DCreateView.as_view(),
        name='model_3d_create'),
]

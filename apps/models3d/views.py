from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Model3D
from .forms import Model3dCreateForm
from userena.utils import get_user_profile


class Model3DCreateView(LoginRequiredMixin, CreateView):
    model = Model3D
    form_class = Model3dCreateForm
    template_name = "models3d/model3d_create.html"

    def get_form_kwargs(self, *args, **kwargs):
        self.profile = get_user_profile(self.request.user)
        form_kwargs = super(Model3DCreateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['profile'] = self.profile
        return form_kwargs

    def get_success_url(self, *args, **kwargs):
        return reverse('profile_detail', kwargs={"username": self.request.user.username})

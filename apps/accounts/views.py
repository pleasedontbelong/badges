from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from userena import settings as userena_settings
from userena.utils import get_user_profile
from django.core.exceptions import PermissionDenied


class ProfileDetailView(DetailView):

    template_name = userena_settings.USERENA_PROFILE_DETAIL_TEMPLATE

    def get_object(self, queryset=None):
        user = get_object_or_404(get_user_model(), username__iexact=self.kwargs['username'])
        self.profile = get_user_profile(user=user)

        if not self.profile.can_view_profile(self.request.user):
            raise PermissionDenied

        self.profile.increment_nb_views()

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        context['profile'] = self.profile
        context['hide_email'] = userena_settings.USERENA_HIDE_EMAIL
        return context

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/profile.html'

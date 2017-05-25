# Create your views here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import get_template
from django.views import generic

from . import auth_views as views
from .forms import AuthenticationForm
from .forms import RegisterUserForm
from .models import RegisterUser


class AnonymousRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        """Comprueba que sea un usuario anónimo o lo redireccionara
        a la pagina LOGIN_REDIRECT_URL
        """
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)


class RegisterUserFormView(AnonymousRequiredMixin, generic.CreateView):
    """Muestra el formulario de registro."""
    model = RegisterUser
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'

    def __init__(self, *args, **kwargs):
        """Elimina posibles usuarios expirados."""
        RegisterUser.delete_expired_registers()
        return super().__init__(*args, **kwargs)

    def get_success_url(self):
        self._send_email_with_token()
        return reverse('authentication:success')

    def _send_email_with_token(self):
        """Envía un email con token para terminar proceso de registro."""
        current_site = get_current_site(self.request)
        site_name = current_site.name
        self_object = self.object
        url_validate_token = reverse(
            'authentication:validate_token',
            kwargs={'token': self_object.token}
        )
        if not current_site.domain.startswith('http'):
            protocol = '{}://'.format('https' if self.request.is_secure() else 'http')
            url_validate_token = '{}{}{}'.format(protocol, current_site.domain, url_validate_token)
        else:
            url_validate_token = '{}{}'.format(current_site.domain, url_validate_token)
        context = {
            'username': self_object.username,
            'email': self_object.email,
            'site_name': site_name,
            'url_validate_token': url_validate_token
        }
        email_template = get_template('authentication/emails/register_success.txt').render(context)
        send_mail(
            subject='Validación de email en {}'.format(site_name),
            message=email_template,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self_object.email]
        )


class RegisterUserSuccessView(AnonymousRequiredMixin, generic.TemplateView):
    template_name = 'authentication/success.html'


class RegisterUserValidateTokenView(AnonymousRequiredMixin, generic.TemplateView):
    template_name = 'authentication/validate_token.html'

    def get(self, request, *args, **kwargs):
        RegisterUser.delete_expired_registers()
        token = self.kwargs.get('token')
        try:
            user_temp = RegisterUser.objects.get(token=token)
        except RegisterUser.DoesNotExist:
            return render(request, 'authentication/token_not_exists.html')
        self._move_user_temp_to_user(user_temp)
        return super().get(request, *args, **kwargs)

    def _move_user_temp_to_user(self, user_temp):
        """Mueve usuario temporal a auth_user y elimina el temporal."""
        user_model = get_user_model().objects.create(
            username=user_temp.username,
            email=user_temp.email,
            password=user_temp.password
        )
        if user_model:
            user_temp.delete()


class LoginView(AnonymousRequiredMixin, views.LoginView):
    template_name = 'authentication/login.html'
    form_class = AuthenticationForm


class LogoutView(LoginRequiredMixin, views.LogoutView):
    template_name = 'authentication/logged_out.html'


class PasswordResetView(AnonymousRequiredMixin, views.PasswordResetView):
    template_name = 'authentication/password_reset_form.html'
    email_template_name = 'authentication/password_reset_email.html'
    subject_template_name = 'authentication/password_reset_subject.txt'
    success_url = reverse_lazy('authentication:password_reset_done')


class PasswordResetDoneView(AnonymousRequiredMixin, views.PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'


class PasswordResetConfirmView(AnonymousRequiredMixin, views.PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('authentication:password_reset_complete')


class PasswordResetCompleteView(AnonymousRequiredMixin, views.PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'authentication/password_change_form.html'
    success_url = reverse_lazy('authentication:password_change_done')


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'
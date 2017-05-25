from django.conf.urls import url

from . import views

app_name = 'authentication'

urlpatterns = [
    # /auth/register/
    # Muestra el formulario de registro.
    url(
        regex=r'^register/$',
        view=views.RegisterUserFormView.as_view(),
        name='register'
    ),

    # /auth/register/success/
    # El registro ha sido satisfactorio.
    url(
        regex=r'^register/success/$',
        view=views.RegisterUserSuccessView.as_view(),
        name='success'
    ),

    # /auth/register/validate/:<str:32>token/
    # Valida un token.
    url(
        regex=r'^register/validate/(?P<token>[a-zA-Z0-9]{32})/$',
        view=views.RegisterUserValidateTokenView.as_view(),
        name='validate_token'
    ),

    # /auth/login/
    # Formulario login.
    url(
        regex=r'^login/$',
        view=views.LoginView.as_view(),
        name='login'
    ),

    # /auth/logout/
    # Loout
    url(
        regex=r'^logout/$',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    # /auth/password_change/
    # Formulario cambiar contraseña.
    url(
        regex=r'^password_change/$',
        view=views.PasswordChangeView.as_view(),
        name='password_change'
    ),

    # /auth/password_change/done/
    # Muestra mensaje cambio password ok.
    url(
        regex=r'^password_change/done/$',
        view=views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    # /auth/password_reset/
    # Restablecer contraseña (Contraseña olvidada).
    url(
        regex=r'^password_reset/$',
        view=views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    # /auth/password_reset/done/
    # Informa al usuario que se ha mandado un email para restablecer la contraseña.
    url(
        regex=r'^password_reset/done/$',
        view=views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    # /auth/reset/:<uidb64>/:<token>/
    # Verifica el token, se accede desde el email.
    # Si es correcto, mostrara un formulario para crear nueva contraseña.
    url(
        regex=(
            r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
            r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'
        ),
        view=views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    # /auth/reset/done/
    # El token se ha verificado y muestra el resultado,
    url(
        regex=r'^reset/done/$',
        view=views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
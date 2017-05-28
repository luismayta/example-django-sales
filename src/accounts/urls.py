from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/profile/
    # Perfil privado de usuario.
    url(
        regex=r'^profile/$',
        view=views.UserProfileView.as_view(),
        name='profile'
    ),

]

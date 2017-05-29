from django.conf.urls import url

from .views import HomeView, LoginView, LogoutView, SignupView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]

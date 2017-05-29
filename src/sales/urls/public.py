from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomeView


urlpatterns = [
    ##################################################
    # / Home page.
    url(r'^$', HomeView.as_view(), name='home_page'),
    ##################################################
    # /home/*
    url(r'^home/', include('home.urls')),
    # api
    url(r'^admin/', admin.site.urls),
]

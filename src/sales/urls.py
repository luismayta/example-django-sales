"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from home.views import IndexView

# from rest_framework import routers

# router = routers.DefaultRouter()

urlpatterns = [
    ##################################################
    # / Home page.
    url(r'^$', IndexView.as_view(), name='home_page'),
    ##################################################

    # /home/*
    url(r'^home/', include('home.urls')),
    # /auth/*
    url(r'^auth/', include('authentication.urls')),
    # /accounts/*
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    # Browsable API.
    # url(r'^api/', include(router.urls)),
]

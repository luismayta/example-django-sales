"""Backend URL Configuration

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
from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from apps.home.views import IndexView
from django.conf import settings

urlpatterns = [

    ##################################################
    # / Home page.
    url(r'^$', IndexView.as_view(), name='home_page'),
    ##################################################

    # /home/*
    url(r'^home/', include('apps.home.urls')),
    # /auth/*
    url(r'^auth/', include('apps.authentication.urls')),
    # /accounts/*
    url(r'^accounts/', include('apps.accounts.urls')),

    # /admin/*
    url(r'^admin/', admin.site.urls),

    ###################################################
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(
        # /media/:<mixed>path/
        url(
            regex=r'^media/(?P<path>.*)$',
            view=serve,
            kwargs={'document_root': settings.MEDIA_ROOT}
        )
    )

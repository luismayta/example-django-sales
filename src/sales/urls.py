from customuser.views import MyUserViewSet, ObtainAuthToken
from django.conf.urls import include, url
from django.contrib import admin
from home.views import HomeView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('users', MyUserViewSet)

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),
    # Browsable API.
    url(r'^api/', include(router.urls)),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework',
        )
    ),
    # Token authentication.
    url(r'^api-token-auth/', ObtainAuthToken.as_view()),
    # Home page.
    url(r'^$', HomeView.as_view(), name='home_page'),
    ##################################################
    # /home/*
    url(r'^home/', include('home.urls')),
]

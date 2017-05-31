from customuser.views import MyUserViewSet, ObtainAuthToken
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
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
    # Core app.
    url(r'^', include('home.urls', namespace='home_app')),
]

# The following enable structural 'static' files while in development mode.
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

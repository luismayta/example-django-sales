from django.conf.urls import include, url

from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    # Browsable API.
    url(r'^api/', include(router.urls)),
]

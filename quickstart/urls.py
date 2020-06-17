from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart.views import *

from quickstart import views
from quickstart import urls


router = routers.DefaultRouter()

router.register(r"users", views.UserViewSet, basename="users")
router.register(r"groups", views.GroupViewSet, basename="groups")
router.register(r"manufacturer", views.ManufacturerViewSet, basename="manufacturer")
router.register(r"shoetype", views.ShoeTypeViewSet)
router.register(r"shoecolor", views.ShoeColorViewSet)
router.register(r"shoe", views.ShoeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace="rest_framework")),
]
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
# from quickstart.views import *

from quickstart import views



router = routers.DefaultRouter()


router.register(r"manufacturer", views.ManufacturerViewSet, basename="manufacturer")
router.register(r"shoetype", views.ShoeTypeViewSet)
router.register(r"shoecolor", views.ShoeColorViewSet)
router.register(r"shoe", views.ShoeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]


from django.contrib import admin
from django.urls import path
from quickstart.urls import urlpatterns as quickstart_urls
from quickstart.models import *

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += quickstart_urls


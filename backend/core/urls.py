
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("", include("apps.users.urls")),
]

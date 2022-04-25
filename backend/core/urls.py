
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from apps.users.views import Login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name="Login"),
    re_path("", include("apps.users.urls")),
]

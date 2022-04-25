from django.urls import include, path
from rest_framework import routers

#from .views import UserViewSet

router = routers.DefaultRouter()

#router.register("API/v1/users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
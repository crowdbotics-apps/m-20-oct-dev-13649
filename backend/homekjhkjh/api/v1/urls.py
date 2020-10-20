from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HGFHJGJHGViewSet

router = DefaultRouter()
router.register("hgfhjgjhg", HGFHJGJHGViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

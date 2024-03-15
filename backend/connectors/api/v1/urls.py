from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134498ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134498", Testconnectors134498ViewSet, basename="testconnectors134498"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

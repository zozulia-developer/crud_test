from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PersonViewSet, TeamViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'people', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

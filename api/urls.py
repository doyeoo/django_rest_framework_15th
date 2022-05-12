from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
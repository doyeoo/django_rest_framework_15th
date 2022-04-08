from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostView)
router.register('profile', ProfileView)

urlpatterns = [
    path('', include(router.urls)),
]
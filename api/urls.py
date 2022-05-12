from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/posts/', post_list),
    path('api/posts/<int:pk>', post_detail),
]
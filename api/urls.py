from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/posts/', PostList.as_view()),
    path('api/posts/<int:pk>', PostDetail.as_view()),
]
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend


class ProfileUpdatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        id = request.GET['id']
        blocked = Profile.objects.filter(id=id).exists()
        return not blocked


class PostFilter(FilterSet):
    user = filters.NumberFilter(field_name='user')
    like_count = filters.NumberFilter(field_name='like_count', lookup_expr='gt')

    class Meta:
        model = Post
        fields = ['user', 'like_count']


class ProfileFilter(FilterSet):
    username = filters.CharFilter(field_name='username', method='filter_username')
    image = filters.BooleanFilter(field_name='image_url', lookup_expr='isnull')

    class Meta:
        model = Profile
        fields = ['username', 'image']

    def filter_username(self, queryset, name, value):
        filtered_queryset = queryset.filter(user__username__contains=value)
        return filtered_queryset


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = PostFilter


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = ProfileFilter


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework import viewsets

class PostView(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.all()


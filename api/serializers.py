from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comment=CommentSerializer(many=True, read_only=True)
    like=LikeSerializer(many=True, read_only=True)
    file=FileSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

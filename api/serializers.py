from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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
    comment = CommentSerializer(many=True, read_only=True)
    like = LikeSerializer(many=True, read_only=True)
    file = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def validate_phone(self, value):
        for char in value:
            if not char.isdigit():
                raise ValidationError("잘못된 형식입니다.")
        return value

    class Meta:
        model = Profile
        fields = ('user', 'username', 'phone', 'image_url', 'website', 'bio', 'follower', 'following')


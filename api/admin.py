from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone']
    list_display_links = ['id', 'user']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content']
    list_display_links = ['id', 'content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_post']
    list_display_links = ['id', 'get_post']

    def get_post(self, obj):
        return obj.post.content

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_post']
    list_display_links = ['id', 'get_post']

    def get_post(self, obj):
        return obj.post.content
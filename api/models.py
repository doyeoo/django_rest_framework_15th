from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=50)
    image=models.ImageField()
    website=models.TextField()
    bio=models.TextField()

    def __str__(self):
        return self.nickname

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    upload_at=models.DateTimeField(auto_now=True)
    likes=models.PositiveIntegerField()
    comments=models.PositiveIntegerField()

    def __str__(self):
        return self.content

class Like(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    upload_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    upload_at=models.DateTimeField(auto_now=True)
    content=models.TextField()

class File(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    file=models.FileField()
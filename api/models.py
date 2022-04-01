from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=50)
    image=models.ImageField(null=True, blank=True)
    website=models.TextField(null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    follower=models.ManyToManyField('self',null=True, blank=True)
    following=models.ManyToManyField('self',null=True, blank=True)

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
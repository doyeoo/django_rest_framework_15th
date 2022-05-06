from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    follower = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content[:50]

class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.content[:50]

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.post.content[:50]

class File(models.Model):
    post = models.ForeignKey(Post, related_name='file', on_delete=models.CASCADE)
    url = models.CharField(max_length=500)

    def __str__(self):
        return self.post.content[:50]
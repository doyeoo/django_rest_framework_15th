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
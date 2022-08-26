
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here



class Profile(models.Model):
    full_name = models.CharField(max_length=200, null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default.jpg',null=True)


    def __str__(self) -> str:
        return self.full_name


class Topic(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
class Blog(models.Model):

    title = models.CharField(max_length=200, null=False)

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:500]
    
    class Meta:
        ordering = ['-created', '-updated']



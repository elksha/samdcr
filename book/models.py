from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    reviewb = models.TextField()
    picture = models.FileField(null=True, blank=True, default='static/error.jpg')
    pictureb = models.FileField(null=True, blank=True, default='static/error.jpg')
    author = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.CharField(max_length=50, default="")
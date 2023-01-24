from django.db.models.deletion import CASCADE
from django.db import models
from django.db.models.fields.related import OneToOneField


class Post (models.Model):
    Image = models.ImageField(upload_to='post_image/%y/%m/%d/')
    title = models.CharField(max_length=300)
    content = models.TextField()
    like= models.BooleanField(default=False) #참거짓 

class Comment (models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    comment =models.TextField()
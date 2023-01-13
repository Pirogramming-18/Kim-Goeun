from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200,null=True)
    pic = models.ImageField(upload_to='templates/image',blank=True, default='')
    year = models.IntegerField(null=True)
    genre = models.CharField(null=True, max_length=20)
    star = models.FloatField(null=True)
    time = models.IntegerField(null=True)
    review = models.TextField(null=True)
    director = models.CharField(max_length=30, null=True)
    actor = models.CharField(max_length=100, null=True)
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
from django.db import models
from django.conf import settings

class Post(models.Model):
    
    Tool_CHOICES = (
        ('django', 'django'), 
        ('react', 'react'),
        ('Spring','Spring'),
        ('Node.js','Node.js'),
        ('Java','Java'),
        ('C++','C++'),
                    )
    title = models.CharField(max_length=64)
    content = models.TextField()
    devtool = models.CharField(max_length=16, choices=Tool_CHOICES, null=True, blank=True)
    interest = models.IntegerField()
    photo= models.ImageField(blank=True, upload_to='posts/%Y%m%d')
from django.db import models
from django.conf import settings


class Tool(models.Model):
    name= models.CharField(max_length=30)
    type= models.CharField(max_length=30)
    tool_content=models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    
    title = models.CharField(max_length=64)
    content = models.TextField()
    devtool = models.ForeignKey("Tool", related_name="Tool", on_delete=models.CASCADE, null=True)
    interest = models.IntegerField()
    photo= models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    
    def __str__(self):
        return self.title
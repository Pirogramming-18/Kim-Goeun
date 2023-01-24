from django.contrib import admin
from .models import Post,Comment

# Register your models here.

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    pass

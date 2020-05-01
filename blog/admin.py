from django.contrib import admin
from .models import Post, Comment

# Register your models here.


# Registering Post model
admin.site.register(Post)


# Registering Comment model
admin.site.register(Comment)
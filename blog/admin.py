from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
# Register your models here.

# Registering Post model
admin.site.register(Post, PostAdmin)


# Registering Comment model
admin.site.register(Comment)
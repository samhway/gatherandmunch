from django.contrib import admin

# Register your models here.

from .models import post, postImage, category

admin.site.register(post)
admin.site.register(postImage)
admin.site.register(category)
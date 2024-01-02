from django.contrib import admin

from .models import Category, Blog, Comment, Likes, PostViews

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(PostViews)
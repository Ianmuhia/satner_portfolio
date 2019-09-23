from django.contrib import admin
from .models import Category, Post, Comment, Project

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Project)

from django.db import models

from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    Title = models.CharField(max_length=30)

    def __str__(self):
        return self.Title


class Post(models.Model):
    Title = models.TextField(blank=False)
    categories = models.ManyToManyField(Category)
    Description = models.TextField(blank=False)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image')
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    Featured = models.BooleanField(default=False)
    sub_image_one = models.ImageField(upload_to='image', blank=True)
    sub_image_two = models.ImageField(upload_to='image', blank=True)
    previous_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name="previous")
    next_post = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name="next")


    def __str__(self):
        return self.Title


    def get_absolute_url(self):
        return reverse('blog_single', kwargs={
            'id': self.id
        })
        
class Comment(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username


project_choices = [
    ('All', 'All'),
    ('upcoming', 'upcoming'),
    ('following', 'following'),
    ('latest', 'latest')
]

class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='project_images')
    category = models.CharField(max_length=20, choices=project_choices)

    def __str__(self):
        return self.title
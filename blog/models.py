from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
      

class Blog(models.Model):

    STATUS = (
        ('Draft', 'd'),
        ('Published', 'p'),
    )

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=15, choices=STATUS, default='d')

    def __str__(self):
        return f'{self.title} - {self.category}'
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time_stamp = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} - {self.content}'


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='like')
    likes = models.BooleanField()


class PostViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_view')
    post_views = models.BooleanField()
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_views
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    likes = models.ManyToManyField('accounts.User', related_name='blog_post')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
#     name = models.CharField(max_length=150)
#     body = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '%s %s' % (self.post.title, self.name)
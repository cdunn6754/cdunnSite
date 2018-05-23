from django.db import models
from django.urls import reverse, reverse_lazy

from blogUser.models import BlogUser

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.SET_NULL,
        null = True
    )

    title = models.CharField(max_length = 250)

    user_markdown = models.TextField()

    def get_absolute_url(self):
        return reverse('blogPost:blogPostDetail', args=(self.pk,))
            #'blogPost:blogPostDetail', args=(self.pk))

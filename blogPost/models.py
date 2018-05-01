from django.db import models
from django.urls import reverse

from blogUser.models import BlogUser

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.SET_NULL,
        null = True
    )

    user_markdown = models.TextField()

    def get_absolute_url(self):
        return reverse('main_index')

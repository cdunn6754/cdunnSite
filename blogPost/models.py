from django.db import models
from django.urls import reverse, reverse_lazy

from blogUser.models import BlogUser

# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length = 250)

    user_markdown = models.TextField()

    def get_absolute_url(self):
        return reverse('blogPost:blogPostDetail', args=(self.pk,))

class BlogComment(models.Model):
    blog_post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE
    )

    author = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE
    )

    comment_body = models.CharField(max_length = 1000)

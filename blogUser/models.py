from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )

    qualifications = models.CharField(max_length=255)

    def __str__(self):
        return (self.user.first_name + self.user.last_name)

class Blog(models.Model):
    written_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = models.TextField()

    author = models.ForeignKey(
        BlogUser,
        on_delete=models.SET_NULL,
        null=True,
        )

    def __str__(self):
        return self.title

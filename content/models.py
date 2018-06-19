from django.db import models

# Create your models here.
class contentPost(models.Model):

    title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)

    body = models.TextField()

    image = models.ImageField(upload_to="contentPostImages")

    creation_date = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    contentTopics = models.ManyToManyField(contentTopic)


class contentTopic(models.Model):

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

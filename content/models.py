from django.db import models
from django.utils import timezone
from django.urls.base import reverse

# Create your models here.

class ContentTopic(models.Model):

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return "ContentTopic: {}".format(self.name)

class ContentPost(models.Model):

    title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)

    heading_image = models.ImageField(upload_to="heading_images")
    template_file = models.FileField(upload_to="template_files")


    creation_date = models.DateField(default=timezone.now)
    date_modified = models.DateField(auto_now=True)

    contentTopics = models.ManyToManyField(ContentTopic)

    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('content:post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return "ContentPost: {}".format(self.title)

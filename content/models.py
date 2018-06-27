from django.db import models

# Create your models here.

class ContentTopic(models.Model):

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return "ContentTopic: {}".format(self.name)

class ContentPost(models.Model):

    title = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)

    body = models.TextField()

    image = models.ImageField(upload_to="ContentPostImages")

    creation_date = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    contentTopics = models.ManyToManyField(ContentTopic)

    def get_absolute_url(self):
        return reverse('blogPost:blogPostDetail', args=(self.pk,))

    def __str__(self):
        return "ContentPost: {}".format(self.title)

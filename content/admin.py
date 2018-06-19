from django.contrib import admin

# Register your models here.
from content.models import ContentPost, ContentTopic

# Register your models here.
admin.site.register(ContentPost)
admin.site.register(ContentTopic)

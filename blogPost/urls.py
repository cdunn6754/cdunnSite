from django.conf.urls import url

from blogPost.views import BlogCreateView

urlpatterns = [
    url(r'^create_blog_post', BlogCreateView.as_view(), name='createBlog'),
]

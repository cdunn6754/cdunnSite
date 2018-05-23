from django.conf.urls import url

from blogPost.views import BlogCreateView, BlogPostDetailView

urlpatterns = [
    url(r'^create_blog_post', BlogCreateView.as_view(), name='createBlog'),
    url(r'^blog_post/(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='blogPostDetail'),
]

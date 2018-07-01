from django.conf.urls import url

from blogPost.views import BlogCreateView, BlogPostDetailView, BlogPostListView

app_name='blogPost'

urlpatterns = [
    url(r'^create_blog_post', BlogCreateView.as_view(), name='createBlog'),
    url(r'^blog_post_detail/(?P<pk>\d+)/$', BlogPostDetailView.as_view(), name='blogPostDetail'),
    url(r'^blog_post_list$', BlogPostListView.as_view(), name='blogPostList'),
]

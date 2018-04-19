from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'blog/blog_index.html'

class AboutMeView(TemplateView):
    template_name = 'blog/about_me.html'

class TestBlogView(TemplateView):
    template_name = 'blog/test_blog.html'

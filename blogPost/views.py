from django.shortcuts import render
from django.views.generic.edit import CreateView

from blogPost.models import BlogPost

# Create your views here.
# def blogIndex(request):
#     return render(request, "blogPost/blog_index.html")

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blogPost/blog_post_form.html"

    fields = "__all__"

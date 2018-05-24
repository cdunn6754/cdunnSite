from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from blogPost.models import BlogPost

# Create your views here.
# def blogIndex(request):
#     return render(request, "blogPost/blog_index.html")

@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blogPost/blog_post_form.html"

    fields = ['user_markdown', 'title']

    def form_valid(self, form):
        print("In form valid fcn")
        form.instance.author = self.request.user.BlogUser
        return super().form_valid(form)

class BlogPostDetailView(DetailView):

    model = BlogPost
    template_name = "blogPost/blog_post_detail.html"

class BlogPostListView(ListView):

    model = BlogPost
    template_name = "blogPost/blog_post_list.html"

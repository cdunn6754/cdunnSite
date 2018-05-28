from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms

from blogPost.models import BlogPost
from blogPost.forms import BlogPostForm

# Create your views here.

@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blogPost/blog_post_form.html"

    #fields = ['user_markdown', 'title']
    form_class = BlogPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user.BlogUser

        # Break file into chunks if necessary to not overload available memory
        if form.cleaned_data['temp_markdown_file'].multiple_chunks():
            while True:
                chunk = form.cleaned_data['temp_markdown_file'].chunk()
                if chunk:
                    form.instance.user_markdown += chunk
                else:
                    break
        else:
            form.instance.user_markdown = form.cleaned_data['temp_markdown_file'].read()
        return super().form_valid(form)

class BlogPostDetailView(DetailView):

    model = BlogPost
    template_name = "blogPost/blog_post_detail.html"

class BlogPostListView(ListView):

    model = BlogPost
    template_name = "blogPost/blog_post_list.html"

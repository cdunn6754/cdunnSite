from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms

from blogPost.models import BlogPost
from blogPost.forms import BlogPostForm, BlogCommentForm

# Create your views here.

@method_decorator(login_required, name='dispatch')
class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blogPost/blog_post_form.html"

    #fields = ['user_markdown', 'title']
    form_class = BlogPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user.blogUser

        # Break file into chunks if necessary to not overload available memory
        # Eventually I would like to render the markdown on the same page
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

# class BlogPostDetailView(DetailView):
#
#     model = BlogPost
#     template_name = "blogPost/blog_post_detail.html"

class BlogPostDetailView(FormMixin, DetailView):

    model = BlogPost
    form_class = BlogCommentForm
    template_name = "blogPost/blog_post_detail.html"

    # Set the author and blog_post automatically
    def form_valid(self, form):
        form.instance.author = self.request.user.blogUser
        form.instance.blog_post = self.object

    # want to reload this page after success
    def get_success_url(self):
        return reverse_lazy('blogPost:blogPostDetail', args=(self.object.pk))

class BlogPostListView(ListView):

    model = BlogPost
    template_name = "blogPost/blog_post_list.html"

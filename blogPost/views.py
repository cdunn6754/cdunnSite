from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms

from blogPost.models import BlogPost, BlogComment
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


class BlogPostDetailView(FormMixin, DetailView):

    model = BlogPost
    form_class = BlogCommentForm
    template_name = "blogPost/blog_post_detail.html"


    # get the comments to display below the post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = BlogComment.objects.filter(blog_post=self.object).order_by("date_created")
        return context

    # Set the author and blog_post automatically
    def form_valid(self, form):
        form.instance.author = self.request.user.blogUser
        form.instance.blog_post = self.object
        form.save()
        return super(BlogPostDetailView, self).form_valid(form)

    # want to reload this page after success
    def get_success_url(self):
        return reverse('blogPost:blogPostDetail', args=(self.object.pk,))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class BlogPostListView(ListView):

    model = BlogPost
    template_name = "blogPost/blog_post_list.html"

class LandingPageView(ListView):

    model = BlogPost
    template_name = "blogPost/landing_page.html"

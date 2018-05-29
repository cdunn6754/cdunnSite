from django.forms import ModelForm
from django import forms

from blogPost.models import BlogPost, BlogComment

class BlogPostForm(ModelForm):
    template_name = "blogPost/blog_post_form.html"
    temp_markdown_file = forms.FileField(label="Markdown File")

    class Meta:
        model = BlogPost
        fields = ['title']

class BlogCommentForm(ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment_body',]

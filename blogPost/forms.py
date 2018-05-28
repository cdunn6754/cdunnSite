from django.forms import ModelForm
from django import forms

from blogPost.models import BlogPost

class BlogPostForm(ModelForm):
    template_name = "blogPost/blog_post_form.html"
    temp_markdown_file = forms.FileField(label="Markdown File")

    class Meta:
        model = BlogPost
        fields = ['title']

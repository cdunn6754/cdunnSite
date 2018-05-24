from django.forms import ModelForm

from blogPost.models import BlogPost

class BlogPostForm(ModelForm):
    template_name = "blogPost/blog_post_form/html"
    class Meta:
        model = BlogPost
        fields = [user_markdown]

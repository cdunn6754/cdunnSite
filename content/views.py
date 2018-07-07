from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from content.models import ContentPost

# Create your views here.
class LandingPageView(ListView):

    model = ContentPost
    template_name = "content/landing_page.html"

class ContentPostDetailView(DetailView):
    model = ContentPost
    template_name = "content/post_detail.html"

class ContentPostListView(ListView):
    model = ContentPost
    template_name = "content/post_list.html"

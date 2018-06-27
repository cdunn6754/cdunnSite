from django.shortcuts import render
from django.views.generic.list import ListView

from content.models import ContentPost

# Create your views here.
class LandingPageView(ListView):

    model = ContentPost
    template_name = "content/landing_page.html"

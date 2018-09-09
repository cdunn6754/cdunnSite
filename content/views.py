from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import Template, Context


from content.models import ContentPost

# Create your views here.
class LandingPageView(ListView):

    model = ContentPost
    template_name = "content/landing_page.html"

class ContentPostDetailView(DetailView):
    model = ContentPost
    template_name = "content/post_detail.html"

    def get_context_data(self, **kwargs):

        context=super(ContentPostDetailView, self).get_context_data(**kwargs)
        slug = context["contentpost"].slug
        context["post_file_path"] = "content/post_html/{}.html".format(slug)

        return context


class ContentPostListView(ListView):
    model = ContentPost
    template_name = "content/post_list.html"

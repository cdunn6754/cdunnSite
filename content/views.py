from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import Template, Context
from django.conf import settings

from content.models import ContentPost

# Create your views here.
class LandingPageView(ListView):

    model = ContentPost
    template_name = "content/landing_page.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        ordered_queryset = ContentPost.objects.order_by("-creation_date")
        context['ordered_posts'] = ordered_queryset
        context['limited_ordered_posts'] = ordered_queryset[:4]
        return context

class ContentPostDetailView(DetailView):
    model = ContentPost
    template_name = "content/post_detail.html"

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)

        # Get path to the correct template file and store so it can be
        # included in post_detail template
        template_file = "media/{}".format(context["contentpost"].template_file)
        with open(template_file,'rt') as f:
            file_content = f.read()

        context["post_template"]=Template(file_content)

        return context


class ContentPostListView(LandingPageView):
    model = ContentPost
    template_name = "content/post_list.html"

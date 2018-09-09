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

        # t = Template(context['contentpost'].body)
        # c = Context(context)
        # rendered_body = t.render(c)
        # context['rendered_body'] = rendered_body

        context["file_name"] = "content/ec2_post.html"

        return context


class ContentPostListView(ListView):
    model = ContentPost
    template_name = "content/post_list.html"

from django.conf.urls import url
from django.urls import include, path, re_path

from content.views import LandingPageView, ContentPostDetailView

app_name='content'

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    re_path(r'details/(?P<slug>[-\w]+)/', ContentPostDetailView.as_view(), name='post_detail'),
]

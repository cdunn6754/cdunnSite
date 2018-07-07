from django.conf.urls import url
from django.urls import include, path, re_path

from content.views import (LandingPageView, ContentPostDetailView,
            ContentPostListView)

app_name='content'

urlpatterns = [
    url(r'^$', LandingPageView.as_view(), name='landing_page'),
    re_path(r'content/details/(?P<slug>[-\w]+)/', ContentPostDetailView.as_view(), name='post_detail'),
    path("content/list", ContentPostListView.as_view(), name='post_list'),
]

from django.conf.urls import url
from blogUser.views import (IndexView, AboutMeView, TestBlogView,
                        createUser)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about_me/', AboutMeView.as_view(), name='about_me'),
    url(r'^test_blog/', TestBlogView.as_view(), name='test'),
    url(r'^create_user/', createUser, name='create_user'),
]

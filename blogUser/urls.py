from django.conf.urls import url
from blogUser.views import (TestBlogView, createUser)


urlpatterns = [
    url(r'^test_blog/', TestBlogView.as_view(), name='test'),
    url(r'^create_user/', createUser, name='create_user'),
]

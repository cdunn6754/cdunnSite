from django.conf.urls import url
from blogUser.views import (TestBlogView, LoginUserView, createUser)


urlpatterns = [
    url(r'^test_blog/', TestBlogView.as_view(), name='test'),
    url(r'^create_user/', createUser, name='create_user'),
    url(r'^login_user/', LoginUserView.as_view(), name="login_user"),
]

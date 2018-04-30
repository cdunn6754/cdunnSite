from django.conf.urls import url
from django.contrib.auth import views as auth_views

from blogUser.views import (TestBlogView, LoginUserView, createUser)



urlpatterns = [
    url(r'^test_blog/', TestBlogView.as_view(), name='test'),
    url(r'^create_user/', createUser, name='create_user'),
    url(r'^login_user/', auth_views.LoginView.as_view
            (
                template_name = "blogUser/login_user.html",
                extra_context = {"next":"main_index"}
            ),
            name="login_user"
        ),
]

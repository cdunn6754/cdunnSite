from django.conf.urls import url
from django.contrib.auth import views as auth_views

from blogUser.views import (TestBlogView, LoginUserView, createUser)



urlpatterns = [
    url(r'^test_blog/', TestBlogView.as_view(), name='test'),
    url(r'^create_user/', createUser, name='create_user'),
    url(r'^login_user/', auth_views.LoginView.as_view
            (
                template_name = "blogUser/login_user.html"
            ),
            name="login_user"
        ),
    url(r'^logout_user/', auth_views.LogoutView.as_view
            (
                template_name = "blogUser/logout_user.html"
            ),
            name="logout_user"
        ),
]

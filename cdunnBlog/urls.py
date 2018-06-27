"""cdunnBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from content.views import LandingPageView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LandingPageView.as_view(), name="landing_page"),
    url(r'^about_me$',
        TemplateView.as_view(template_name="static_html/about_me.html"),
        name = "about_me"),
    url(r'^users/', include('blogUser.urls', namespace='blogUser')),
    url(r'^posts/', include('blogPost.urls', namespace='blogPost')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

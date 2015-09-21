"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from posts.views import *
from statics_pages.views import *
import settings
from django.conf.urls.static import static

from actions import setUp

# setUp of the proyect
setUp()

urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')), # texteditor urls
    url(r'^post/', include('posts.urls') ), # url POSTS
    url(r'^page/', include('statics_pages.urls') ), # url PAGES
    url(r'', 'blog.views.home'), # home
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# only dev

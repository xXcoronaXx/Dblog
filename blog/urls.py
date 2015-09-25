from django.conf.urls import include, url
from django.contrib import admin

from posts.views import *
from statics_pages.views import *
import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemap import *
from .feeds import LatestPostFeed
from actions import setUp

# setUp of the proyect
setUp()


urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')), # texteditor urls
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': BlogSitemap(), 'pages': StaticSitemap()}}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^latest/feed/$', LatestPostFeed()),
    url(r'^post/', include('posts.urls') ), # url POSTS
    url(r'^page/', include('statics_pages.urls') ), # url PAGES
    url(r'', 'blog.views.home'), # home
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# only dev

from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/(?P<slug>[\w\-]+)/', 'statics_pages.views.preview_page', name='preview_page'),
    url(r'^(?P<slug>[\w\-]+)/', 'statics_pages.views.view_page', name='view_page'),
]
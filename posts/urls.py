from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/(?P<slug>[\w\-]+)/', 'posts.views.post_preview', name='post_preview'),
    url(r'^tag/(?P<slug>[\w\-]+)/', 'posts.views.posts_view_tag', name='posts_tag'),
    url(r'^popular/', 'posts.views.posts_view_popular', name='posts_popular'),
    url(r'^(?P<slug>[\w\-]+)/', 'posts.views.post_view', name='post_view'),
]
from django.contrib.syndication.views import Feed
from posts.models import Post
from django.contrib.sites.models import Site

class LatestPostFeed(Feed):
	current_site = Site.objects.get_current()
	title = "Hot news" 
	link = "/"
	description = "Updates from %s" % current_site

	def items(self):
	    return Post.objects.order_by('-created')[:5]

	def item_title(self, item):
	    return item.title

	def item_description(self, item):
	    return item.text
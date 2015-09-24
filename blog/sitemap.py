from django.contrib.sitemaps import Sitemap
from posts.models import Post
from statics_pages.models import Page

class BlogSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5

	def items(self):
		return Post.objects.filter(visible=True)[:100]

	def lastmod(self, obj):
		return obj.created

class StaticSitemap(Sitemap):
	changefreq = "monthly"
	priority = 0.5

	def items(self):
		return Page.objects.filter(visible=True)

	def lastmod(self, obj):
		return obj.created
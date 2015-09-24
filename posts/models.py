from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.contrib.sitemaps import ping_google

class Tag(models.Model):
	name = models.CharField(max_length=255)
	slug = AutoSlugField(populate_from='name',unique_with=['id'], blank=True)

	def __str__(self): 
		return self.name

class Post(models.Model):
	author   = models.ForeignKey(User, blank=True)
	title    = models.CharField(max_length=255)
	slug     = AutoSlugField(populate_from='title',unique_with=['id'], blank=True)
	visible  = models.BooleanField(default=False)
	text     = models.TextField()
	created  = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	views    = models.IntegerField(default=0)

	tags     = models.ManyToManyField(Tag)


	def get_absolute_url(self):
		if self.visible:
			return '/post/'+ self.slug +'/' 
		else:
			return '/post/admin/'+ self.slug +'/' 
	
	def __str__(self):
		return self.title

	@staticmethod
	def autocomplete_search_fields():
		return 'title'

	def save(self, force_insert=False, force_update=False):
		super(Post, self).save(force_insert, force_update)
		try:
			ping_google()
		except Exception:
			# Bare 'except' because we could get a variety
			# of HTTP-related exceptions.
			pass
from django.db import models

class FooterURL(models.Model):
	name = models.CharField(max_length=255)
	url = models.CharField(max_length=255)

	def __str__(self): 
		return self.name

class Config(models.Model):
	title               = models.CharField(max_length=255)
	subtitle            = models.CharField(max_length=255)
	seo_description		= models.CharField(max_length=255,blank=True)
	allow_comments      = models.BooleanField(default=True)
	name_Disqus         = models.CharField(max_length=255,blank=True)
	show_popular_link   = models.BooleanField(default=False)
	show_popular_widget = models.BooleanField(default=False)

	def __str__(self): 
		return 'Config'

	def delete(self, *args, **kwargs):
		pass
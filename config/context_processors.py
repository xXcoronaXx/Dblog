from .models import *
from django.conf import settings

def config(request):
	conf = Config.objects.get(pk=1)
	foot = FooterURL.objects.all()
	return { 
			'title': conf.title,
			'subtitle': conf.subtitle,
			'seo_description': conf.seo_description,
			'allow_comments': conf.allow_comments,
			'name_Disqus': conf.name_Disqus,
			'show_popular_link': conf.show_popular_link,
			'show_popular_widget': conf.show_popular_widget,
			'FooterURL': foot,
			'lang': settings.LANGUAGE_CODE,
			'current_path': request.build_absolute_uri(),
			 }
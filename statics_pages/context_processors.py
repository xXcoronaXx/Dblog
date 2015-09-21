from .models import *

def statics_pages(request):
	pages = Page.objects.all().filter(visible=True)
	return { 
			'statics_pages': pages,
			 }
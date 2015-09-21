from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from actions import export_as_excel
from django_summernote.models import Attachment
from .models import *

class PostAdmin(SummernoteModelAdmin):
	list_display = ('title', 'author', 'created', 'views', 'visible')
	list_filter = ('tags',)
	exclude = ('author',)
	search_fields = ('title', 'author')
	actions = (export_as_excel, )

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
# para no mostrar los datos del editor enriquezido en el admin 
admin.site.unregister(Attachment)
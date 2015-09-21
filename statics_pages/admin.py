from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from actions import export_as_excel
from django_summernote.models import Attachment
from .models import *

class PageAdmin(SummernoteModelAdmin):
	list_display = ('title', 'author', 'created', 'views', 'visible')
	exclude = ('author',)
	search_fields = ('title',)
	actions = (export_as_excel, )

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.save()


admin.site.register(Page, PageAdmin)
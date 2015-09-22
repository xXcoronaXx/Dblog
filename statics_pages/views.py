from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import user_passes_test

def view_page(request, slug):
	page = get_object_or_404( Page, slug=slug, visible=True )
	page.views += 1
	page.save()
	return render(request, 'page.html', { 'page': page })

@user_passes_test(lambda u: u.is_staff)
def preview_page(request, slug):
	page = get_object_or_404( Page, slug=slug, visible=False )

	return render(request, 'page.html', { 'page': page })
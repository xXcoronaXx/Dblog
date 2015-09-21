from django.shortcuts import render, get_object_or_404
from .models import *

from django.contrib.auth.decorators import login_required

def view_page(request, slug):
	page = get_object_or_404( Page, slug=slug, visible=True )
	page.views += 1
	page.save()
	return render(request, 'page.html', { 'page': page })

@login_required
def preview_page(request, slug):
	page = get_object_or_404( Page, slug=slug, visible=False )

	return render(request, 'page.html', { 'page': page })
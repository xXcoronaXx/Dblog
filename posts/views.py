from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from types import NoneType

from .models import *

def post_view(request, slug):
	post = get_object_or_404( Post, slug=slug, visible=True )
	post.views += 1
	post.save()
	return render(request, 'post.html', { 'post': post })

@login_required
def post_preview(request, slug):
	post = get_object_or_404( Post, slug=slug, visible=False )
	return render(request, 'post.html', { 'post': post })

def posts_view_tag(request, slug):
	posts = Post.objects.all().filter(visible=True, tags__slug=slug)
	tag = Tag.objects.get(slug=slug)
	try:
		posts = Paginator(posts,5)
		page = request.GET.get('page')
		posts = posts.page(page)
	except (PageNotAnInteger, NoneType) as e:
		# If page is not an integer, deliver first page.
		posts = posts.page(1)
		page = 1
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = posts.page(posts.num_pages)
	except:
		posts = None
	return render(request, 'posts_tags.html', { 'posts': posts, 'tag': tag })

def posts_view_popular(request):
	posts = Post.objects.all().filter(visible=True).order_by('-views')
	try:
		posts = Paginator(posts,5)
		page = request.GET.get('page')
		posts = posts.page(page)
	except (PageNotAnInteger, NoneType) as e:
		# If page is not an integer, deliver first page.
		posts = posts.page(1)
		page = 1
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = posts.page(posts.num_pages)
	except:
		posts = None
	return render(request, 'posts_popular.html',{ 'posts': posts })
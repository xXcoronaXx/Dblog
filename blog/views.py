from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from types import NoneType
from posts.models import Post

def home(request):
	try:
		post_new = Post.objects.all().filter(visible=True).latest('created')
		posts = Post.objects.all().filter(visible=True).exclude(id__in=[post_new.id])

		popular = Post.objects.all().filter(visible=True).order_by('-views')
		popular = popular[0]

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
		post_new = None
		posts = None
		popular = None
	
	return render(request, 'index.html', { 'posts': posts, 'post_new': post_new, 'popular': popular })
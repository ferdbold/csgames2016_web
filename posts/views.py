from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
	latest_posts = Post.objects.order_by('-pub_date')[:5]
	context = {
		'latest_posts': latest_posts
	}

	return render(request, 'posts/index.html', context)

def single(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {
		'post': post
	}

	return render(request, 'posts/single.html', context)

def profile(request, user_id):
	context = {}
	return render(request, 'posts/profile.html', context)

def new(request):
	context = {}
	return render(request, 'posts/new.html', context)

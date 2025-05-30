from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django .http import Http404
from django.core.paginator import Paginator

# Create your views here.

# posts=[
#         {'id':1, 'title': 'post 1', 'content': 'content 1'},
#         {'id':2, 'title': 'post 2', 'content': 'content 2'},
#         {'id':3, 'title': 'post 3', 'content': 'content 3'},
#         {'id':4, 'title': 'post 4', 'content': 'content 4'},
#     ]

# getting data from db
posts=Post.objects.all()

def index (request):
    title = 'portfolio gokul'

    paginator=Paginator(posts, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'hi.html', {'title':title , 'page_obj':page_obj})


def post (request , slug):
    # return render(request , 'hello.html' )

    # static field
    # post = next((item for item in posts if item['id'] == post_id ),None)

    try:
        # getting post id 
        # post = Post.objects.get(pk=post_id)
        post = Post.objects.get(slug=slug) 
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404('post does not txit')

    # logger = logging.getLogger('testing')
    # logger.debug(F'post variable is {post}')
    
    return render(request , 'hello.html' , {'post':post, 'related_posts':related_posts})

def old_url (request ) :
    return redirect(reverse('blog:new_page_url'))

def new_url_view (request ) :
    return HttpResponse('i am in new url...') 
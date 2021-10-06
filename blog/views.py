from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

# Collect blog posts from database and render blog page with posts

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('blog/blog.html')
    context = {
        'latest_post_list': latest_post_list,
    }

    return HttpResponse(template.render(context,request))
from django.shortcuts import render,get_object_or_404
from .models import Post

def get_title(post:dict):
    return post['title']


# Create your views here.
def start_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html", {"posts": latest_posts})


def list_posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": all_posts})


def detail_post(request,slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", 
                  {
                      "post":identified_post,
                      "post_tags":identified_post.tags.all()
                   })
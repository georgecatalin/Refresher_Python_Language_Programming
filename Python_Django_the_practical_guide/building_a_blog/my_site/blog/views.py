from django.shortcuts import render

# Create your views here.
def start_page(request):
    return render(request,"blog/index.html")


def list_posts(request):
    return render(request, "blog/all-posts.html")


def detail_post(request,slug):
    return render(request, "blog/post-detail.html")
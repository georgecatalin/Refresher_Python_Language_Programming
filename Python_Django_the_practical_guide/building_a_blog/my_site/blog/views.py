from django.shortcuts import render

# Create your views here.
def start_page(request):
    return render(request,"blog/index.html")


def list_posts(request):
    pass


def detail_post(request):
    pass
from django.shortcuts import render,get_object_or_404
from .models import Book

# Create your views here.
def index(request):
   books = Book.objects.all()
   return render(request,"book_outlet/index.html", {"books" : books})


def get_detail(request, slug):
   book = get_object_or_404(Book,slug=slug)
   return render(request, "book_outlet/book_detail.html" , {
      "title": book.title,
      "rating":book.rating,
      "author":book.author,
      "is_best_seller" : book.is_best_seller
   })
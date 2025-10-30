from django.shortcuts import render,get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
   books = Book.objects.all()
   number_of_books = books.count()
   average_rating = books.aggregate(Avg("rating"))
   
   return render(request,"book_outlet/index.html", {
      "books" : books,
      "total_books" : number_of_books,
      "average_rating" : average_rating
      })


def get_detail(request, slug):
   book = get_object_or_404(Book,slug=slug)
   return render(request, "book_outlet/book_detail.html" , {
      "title": book.title,
      "rating":book.rating,
      "author":book.author,
      "is_best_seller" : book.is_best_seller
   })
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import ReviewForm


# Create your views here.
def display(request):
    if request.method == 'POST':
      
      this_form = ReviewForm(request.POST)

      if this_form.is_valid():
         print(this_form.cleaned_data)
         return HttpResponseRedirect(reverse('thank-you-page'))
      
    this_form = ReviewForm()
    return render(request,"reviews/review.html", {"form":this_form})


def display_thank(request):
    return render(request, 'reviews/thank_you.html')
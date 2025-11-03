from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import ReviewForm
from .models import Review


# Create your views here.
def display(request):
    if request.method == 'POST':
      
      this_form = ReviewForm(request.POST)

      if this_form.is_valid():
         print(this_form.cleaned_data)
 
 
         this_data = Review(
            user_name=this_form.cleaned_data['user_name'],
            text_review =this_form.cleaned_data['text_review'],
            rating = this_form.cleaned_data['rating']
            )
         
         this_data.save()




         return HttpResponseRedirect(reverse('thank-you-page')) 
      
    else:
       this_form = ReviewForm()
    
    return render(request,"reviews/review.html", {"form":this_form})


def display_thank(request):
    return render(request, 'reviews/thank_you.html')
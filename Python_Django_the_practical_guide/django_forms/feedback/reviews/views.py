from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

class ReviewView(View):
   def get(self,request):
       this_form = ReviewForm()
       return render(request,"reviews/review.html", {"form":this_form})


   def post(self,request):
       this_form = ReviewForm(request.POST)

       if this_form.is_valid():
          this_form.save()

       return HttpResponseRedirect(reverse('thank-you-page'))



# Create your views here.
# def display(request):
#     if request.method == 'POST':
      
#       existing_data = Review.objects.get(pk=1) # for updating a certain record
#       this_form = ReviewForm(request.POST, instance=existing_data)

#       if this_form.is_valid():
#          print(this_form.cleaned_data)
 
         # this_data = Review(
         #    user_name=this_form.cleaned_data['user_name'],
         #    text_review =this_form.cleaned_data['text_review'],
         #    rating = this_form.cleaned_data['rating']
         #    )
         
         # this_data.save()

         # this_form.save() # for ModelForms , models are already existing

   #       return HttpResponseRedirect(reverse('thank-you-page')) 
      
   #  else:
   #     this_form = ReviewForm()
    
   #  return render(request,"reviews/review.html", {"form":this_form})

# replace the function with a standard class view
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank_you.html')


# def display_thank(request):
#     return render(request, 'reviews/thank_you.html')


# replace the standard class view with a template view
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Hello from template view."
        return context
    
class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_list = Review.objects.all()
        context["review_list"] = review_list
        return context
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def display(request):
    if request.method == 'POST':
        user_name = request.POST['this_user']
        print(user_name)
        if user_name == "" or len(user_name) > 100:
            return render(request, "reviews/review.html", { "has_error": True})
        return HttpResponseRedirect(reverse('thank-you-page'))

    return render(request,"reviews/review.html", {"has_error":False})


def display_thank(request):
    return render(request, 'reviews/thank_you.html')
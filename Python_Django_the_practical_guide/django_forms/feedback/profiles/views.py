from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfilesForm

# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfilesForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfilesForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            #print(request.FILES["my_file"])
            #store_file(request.FILES["my_file"])
            return HttpResponseRedirect("/profiles")
        
        return render(request,"profiles/create_profile.html", {"form": submitted_form})

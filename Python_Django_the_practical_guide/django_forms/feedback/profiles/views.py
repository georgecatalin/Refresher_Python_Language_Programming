from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfilesForm
from .models import UserModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.

# once saving through the model is ready, there is not need for this function
# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

# Implement using CreateView class
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserModel
    fields = "__all__"
    success_url = "/profiles"



""" 
class CreateProfileView(View):
    def get(self, request):
        form = ProfilesForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfilesForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            #print(request.FILES["my_file"])
            #store_file(request.FILES["my_file"])
            
            # save file to database
            my_model = UserModel(image=request.FILES["user_image"])
            my_model.save()
            return HttpResponseRedirect("/profiles")
        
        return render(request,"profiles/create_profile.html", {"form": submitted_form}) """


# create a List View to display the list of profiles
class UserProfilesView(ListView):
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles_list"
    model = UserModel
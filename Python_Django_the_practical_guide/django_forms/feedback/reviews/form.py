from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="user name", max_length=10, error_messages={ 
#         "required": "You have to enter a name", 
#         "max_length":"You have exceeded the maximum length permitted"
#         })
#     text_review = forms.CharField(label="Your Review", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=10)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
       # fields = ['user_name','text_review','rating']  #these are listed th models whose controls will be created in the form
        fields = '__all__'
       # exclude = ['rating'] # to exclude a certain field
        labels = {
            "user_name" : "Type your name",
            "text-review" : "Type your feedback",
            "rating" : "Type your rating"
        }

        error_messages = {
            "user_name" : {
                "required" : "You gotta enter something",
                "max_length" : "You should not exceed the maximum length"
            }
        }
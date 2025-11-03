from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="user name", max_length=10, error_messages={ 
        "required": "You have to enter a name", 
        "max_length":"You have exceeded the maximum length permitted"
        })
    text_review = forms.CharField(label="Your Review", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=10)
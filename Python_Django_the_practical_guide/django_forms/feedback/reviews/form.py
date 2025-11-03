from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=10, label="user name", required=True, error_messages={"required": "You have to enter a name", "max_length":"You have exceeded the maximul length permitted"})
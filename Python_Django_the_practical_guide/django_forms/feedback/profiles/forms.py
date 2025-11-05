from django import forms

class ProfilesForm(forms.Form):
    #user_image = forms.FileField()
    user_image = forms.ImageField()
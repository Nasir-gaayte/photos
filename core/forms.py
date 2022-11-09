from django import forms
from .models import PhotoModel





class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ("category", "image", "description")
from django import forms
from .models import ImagePost, Tribute

class ImagePostForm(forms.ModelForm):

    class Meta:
        model = ImagePost
        exclude = ['url',]

class Tributeform(forms.ModelForm):

    class Meta:
        model = Tribute
        exclude = ['writer', 'tribute', 'date']

        widgets ={
            'relationship': forms.Select(
                    attrs={
                    'placeholder':"Relationship", 
                    'data-form-field':"email", 
                    'class':"form-control",
                    'id':"email-contact-form-2-u9CjnDUwsQ"
                }
            )
        }
from django import forms
from .models import ImagePost, Tribute

class ImagePostForm(forms.ModelForm):

    class Meta:
        model = ImagePost
        exclude = ['url','caption']

class Tributeform(forms.ModelForm):

    class Meta:
        model = Tribute
        exclude = [ 'date']

        widgets ={
            'writer': forms.TextInput(
                    attrs={
                    'name':"name",
                    'id':"name" ,
                    'class':"d-block w-100 py-3 rounded mb-4" ,
                    'style':"border: solid grey 2px;",
                    'placeholder':"Enter your name",
                }
            ),
            'relationship': forms.Select(
                attrs={
                    'type':"text",
                    'name':"relationship",
                    'id':"relationship",
                    'class':"d-block w-100 py-3 rounded",
                    'style':"border: solid grey 2px;"
                }
            ),
            'tribute': forms.Textarea(
                attrs={
                    'name':"tribute-message",
                    'id':"tribute-message",
                    'cols':"30",
                    'rows':"10",
                    'placeholder':"write your tribute",
                    'class':"w-100",
                    'style':"border: solid grey 2px;"
                }
            )
        }
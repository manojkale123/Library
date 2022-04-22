import imp
from django.core import validators
from django import forms
from .models import Book

class BookRegister(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','isbn','publisher']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'isbn': forms.TextInput(attrs={'class':'form-control'}),
            'publisher': forms.TextInput(attrs={'class':'form-control'}),





        }


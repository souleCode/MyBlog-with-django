
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    title= forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    content=forms.CharField(label='Content ',widget=forms.Textarea(attrs={
        'class':'form-control'
    }))
    class Meta:
        model=Post
        fields=('title','content','image') # on enleve user pour permettre a ce que une fois que
                                          #l'utilisateur remplie c'est son nom qui s'affiche lui mm ne va pas remplir son nom
from django import forms
from .models import Topic, Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'topic', 'description', 'img_src', 'link', 'rating']
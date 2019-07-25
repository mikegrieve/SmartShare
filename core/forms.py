from django import forms
from .models import Topic, Item, Review

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'topic', 'description', 'img_src', 'link', 'rating']

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['item', 'user', 'content', 'score']
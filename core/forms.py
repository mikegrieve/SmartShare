from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Topic, Item, Review

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'topic', 'description', 'img_src', 'link', 'rating']

class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'content', 'score']
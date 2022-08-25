from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Blog


# class UserForm(ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email']


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']
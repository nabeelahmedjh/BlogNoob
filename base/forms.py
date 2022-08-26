from dataclasses import field
from pyexpat import model
from django.forms import ModelForm

from .models import Blog, Profile


# class UserForm(ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email']


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author']

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
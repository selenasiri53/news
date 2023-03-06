from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'age',)

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# Meta allows us to override the default fields
    # set model to CustomUser, set fields via Meta.fields (includes all default fields)
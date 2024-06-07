from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]
        widgets = {
            'image': forms.FileInput(),
            'display_name': forms.TextInput(attrs={'placeholder': 'Add display name'}),
            'info': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add Information'}),
        }


class EmailForm(ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email',]
    
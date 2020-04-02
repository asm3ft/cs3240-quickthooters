from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'major', 'year')

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.major = self.cleaned_data['major']
        user.year = self.cleaned_data['year']
        user.save()
        return user




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['major', 'year', 'image']
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from . import models
from typing import Any

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text=_('''
            Your password can not be too similar to your other personal information,<br> 
            Your password must contain at least 8 characters,<br> 
            Your password can not be a commonly used,<br>
            Your password can not be entirely numeric.''')


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name', 'email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('picture',)


class ChatForm(forms.ModelForm):
    suggested_participants = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Suggested Participants"
    )

    class Meta:
        model = models.Chat
        fields = ('title', 'description', 'image', 'is_private', 'participants')

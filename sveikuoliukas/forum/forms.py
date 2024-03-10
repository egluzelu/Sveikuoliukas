from django import forms
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('body', 'image')

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('name', 'description', 'image')
        
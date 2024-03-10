from django import forms
from . import models


class CommentForm(forms.ModelForm):
    context = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
    }))

    class Meta:
        model = models.Comment
        fields = ('context', )

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('name', 'description', 'image')
        
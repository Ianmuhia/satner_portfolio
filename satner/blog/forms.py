from django import forms
from .models import Comment


class signupForm(forms.Form):
    email = forms.EmailField(max_length=150)


class CommentForm(forms.ModelForm):
    class meta:
        models = Comment
        fields = "content"

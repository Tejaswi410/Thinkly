from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Thought, Comment


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ["display_name", "body", "photo"]
        widgets = {
            "display_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your name"}
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "What are you thinking?",
                }
            ),
            "photo": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "body"]
        widgets = {
            "author_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "body": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Add a comment"}
            ),
        }


class StyledAuthenticationForm(AuthenticationForm):
    """Authentication form with unified styling/placeholder."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Username"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Password"}
        )


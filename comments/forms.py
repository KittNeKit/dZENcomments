from captcha.fields import CaptchaField
from django import forms

from comments.models import Comments


class CommentCreate(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comments
        fields = ["username", "email", "captcha", "text"]
        labels = {
            "content": "Add new comment",
        }

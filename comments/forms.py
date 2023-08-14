from captcha.fields import CaptchaField
from django import forms

from comments.models import Comments


class CommentCreate(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comments
        fields = ["username", "email", "home_page", "captcha", "text", "file"]
        labels = {
            "content": "Add new comment",
        }

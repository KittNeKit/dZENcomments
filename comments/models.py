import os
import uuid

from django.db import models
from django.utils.text import slugify


def comment_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.username)}-{uuid.uuid4()}{extension}"

    return os.path.join("static/comment_files/", filename)


class Comments(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    answer_comment = models.ForeignKey("Comments", on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    home_page = models.URLField(
        blank=True,
        null=True,
    )
    file = models.FileField(
        upload_to=comment_image_file_path,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text

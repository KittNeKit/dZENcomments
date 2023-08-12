from django.db import models


class Comments(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    answer_comment = models.ForeignKey("Comments", on_delete=models.CASCADE, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

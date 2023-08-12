from django.urls import path

from comments.views import CommentsListView

urlpatterns = [
    path("", CommentsListView.as_view(), name="comments_list"),
]

app_name = "comments"

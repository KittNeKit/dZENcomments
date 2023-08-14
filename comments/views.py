from datetime import datetime
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

import bleach

from comments.forms import CommentCreate
from comments.models import Comments

ALLOWED_TAGS = ["a", "code", "i", "strong"]
ALLOWED_ATTRIBUTES = {"a": ["href", "title"]}


class CommentsListView(FormMixin, generic.ListView):
    model = Comments
    queryset = Comments.objects.order_by("-created_time").select_related(
        "answer_comment"
    )
    template_name = "comments/comments_list.html"
    context_object_name = "comments_list"
    paginate_by = 25
    form_class = CommentCreate
    success_url = reverse_lazy("comments:comments_list")

    def get_queryset(self):
        queryset = Comments.objects.all()
        order_by = self.request.GET.get("order_by")
        ordering = self.request.GET.get("order")
        if order_by:
            if ordering == "asc":
                return queryset.order_by(order_by)
            elif ordering == "desc":
                return queryset.order_by(f"-{order_by}")
        return queryset

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        try:
            answer_comment = Comments.objects.get(id=request.POST.get("parent_comment"))
        except:
            answer_comment = None
        file = request.FILES.get("file")
        if file:
            if file.content_type not in [
                "image/jpeg",
                "image/gif",
                "image/png",
                "text/plain",
            ]:
                return HttpResponseBadRequest(content="Bad format for file")

        if form.is_valid():
            text = bleach.clean(
                request.POST["text"], tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES
            )

            Comments.objects.create(
                username=request.POST["username"],
                text=text,
                email=request.POST["email"],
                answer_comment=answer_comment,
                created_time=datetime.now(),
                file=file,
                home_page=request.POST.get("home_page"),
            )
            print("ok")
            return self.form_valid(form)

        return HttpResponseBadRequest(content="Form filed wrong")

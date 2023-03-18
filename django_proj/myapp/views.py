from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, mixins
from .models import Notes, Groups, Tags
from .forms import NoteForm
from django.http import HttpRequest, HttpResponse
from .serializers import NotesSerializer, GroupsSerializer, TagsSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

# from django.views.generic import (
#     ListView,
#     CreateView,
#     DetailView,
#     UpdateView,
#     DeleteView,
# )
# from .filters import ArticleFilterSet
from rest_framework.schemas.openapi import AutoSchema

from django.shortcuts import render, get_object_or_404


@login_required  # If the user isn’t logged in, redirect to settings.LOGIN_URL
def home(request):
    return render(
        request,
        "_index.html",
        {
            "categories": Groups.objects.all().filter(author_id=request.user.id)
            #'categories': Groups.objects.all().filter(author_id=3).order_by("id")
        },
    )


@login_required
def category_detail(request, group_id):
    category = get_object_or_404(
        Groups, id=group_id
    )  # не делаю фильтрацию по пользоватлею, т.к. подразумевается, что id уникальные и не могут дублироваться у пользователей
    return render(request, "detail.html", {"category": category})


@login_required
def tags_detail(request):
    return render(
        request,
        "tags.html",
        {"tags": Tags.objects.all().filter(author_id=request.user.id)},
    )


@login_required
def edit_note_tags(request: HttpRequest, note_id) -> HttpResponse:
    # dictionary for initial data with
    # field names as keys
    context = {}
    note = get_object_or_404(Notes, id=note_id)  # fetch the object related to passed id
    form = NoteForm(
        request.POST or None, instance=note
    )  # pass the object as instance in form
    if request.method == "POST":
        if form.is_valid():
            note = form.save()  # form.save() creates a note from the form
            # return redirect("post_detail", slug=post.slug)
            return redirect("home")
    # context = {"form": form, "note": note, "edit_mode": False}
    # не проверяем наличия request.user.id, т.к. форма отображается только аутентифицированным пользователям
    form.fields["tags"].queryset = Tags.objects.filter(
        author_id=request.user.id
    ).order_by(
        "id"
    )  # в форме отобразим тэги пользователя
    context = {"form": form}
    return render(request, "post_form.html", context)


# class AllTagsListView(ListView):
#     """Представление для отображения списка всех заметок"""
#
#     model = Tags
#     context_object_name = "tags"
#     template_name = "all_tags.html"
#
# class TagDetailView(DetailView):
#     """Представление для отображения одной заметки."""
#
#     model = Tags
#     context_object_name = "tag"
#     template_name = "tag_detail.html"

# class AllNotesListView(ListView):
#     """Представление для отображения списка всех заметок"""
#
#     model = Notes
#     context_object_name = "notes"
#     template_name = "all_notes.html"
#
# class NoteDetailView(DetailView):
#     """Представление для отображения одной заметки."""
#
#     model = Notes
#     context_object_name = "notes"
#     template_name = "note_detail.html"


# ************** DRF*************
class NotesViewSet(
    mixins.ListModelMixin,  # GET /notes
    mixins.CreateModelMixin,  # POST /notes
    mixins.RetrieveModelMixin,  # GET /notes/1
    mixins.DestroyModelMixin,  # DELETE /notes/1
    mixins.UpdateModelMixin,  # PUT /notes/1
    viewsets.GenericViewSet,
):
    #    queryset = Notes.objects.all()
    def get_queryset(self):
        """
        Выборка заметок для аутентифицированного пользователя. Для AnonimousUser:
        SELECT "myapp_notes"."id", "myapp_notes"."created", "myapp_notes"."modified", "myapp_notes"."title", "myapp_notes"."content", "myapp_notes"."author_id_id", "myapp_notes"."tag_id_id", "myapp_notes"."group_id_id" FROM "myapp_notes" WHERE "myapp_notes"."author_id_id" IS NULL
        """
        queryset = (
            Notes.objects.all().filter(author_id=self.request.user.id).order_by("id")
        )
        return queryset

    # def get_queryset(self):
    #     queryset = Article.objects.all().filter(author=self.request.user).order_by("-id")
    #     return queryset
    serializer_class = NotesSerializer
    # pagination_class = BasePageNumberPagination
    # filterset_class = NotesFilterSet
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )  # доступ только после аутентификации и только владельцу записи в БД. Не работает для ListView
    ordering_fields = ["id", "title"]  # Specifying which fields may be ordered against
    ordering = ["id"]  # default ordering

    schema = AutoSchema(
        tags=["Notes"],
        component_name="Notes",
        operation_id_base="Notes",
    )
    # def create(self, request, *args, **kwargs):
    #     #request.data["author"] = request.user.pk
    #     return super().create(request, *args, **kwargs)


class GroupsViewSet(
    mixins.ListModelMixin,  # GET /groups
    mixins.CreateModelMixin,  # POST /groups
    mixins.RetrieveModelMixin,  # GET /groups/1
    mixins.DestroyModelMixin,  # DELETE /groups/1
    mixins.UpdateModelMixin,  # PUT /groups/1
    viewsets.GenericViewSet,
):
    """
    Выборка  групп для аутентифицированного пользователя.
    """

    #    queryset = Notes.objects.all()
    def get_queryset(self):
        queryset = (
            Groups.objects.all().filter(author_id=self.request.user.id).order_by("id")
        )
        return queryset

    # def get_queryset(self):
    #     queryset = Article.objects.all().filter(author=self.request.user).order_by("-id")
    #     return queryset
    serializer_class = GroupsSerializer
    # pagination_class = BasePageNumberPagination
    # filterset_class = NotesFilterSet
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )  # доступ только после аутентификации и только владельцу записи в БД. Не работает для ListView
    ordering_fields = ["id", "name"]  # Specifying which fields may be ordered against
    ordering = ["id"]  # default ordering

    schema = AutoSchema(
        tags=["Groups"],
        component_name="Groups",
        operation_id_base="Groups",
    )

    # def create(self, request, *args, **kwargs):
    #     # request.data["author"] = request.user.pk
    #     return super().create(request, *args, **kwargs)


class TagsViewSet(
    mixins.ListModelMixin,  # GET /tags
    mixins.CreateModelMixin,  # POST /tags
    mixins.RetrieveModelMixin,  # GET /tags/1
    mixins.DestroyModelMixin,  # DELETE /tags/1
    mixins.UpdateModelMixin,  # PUT /tags/1
    viewsets.GenericViewSet,
):
    """
    Выборка  тэгов для аутентифицированного пользователя.
    """

    def get_queryset(self):
        queryset = (
            Tags.objects.all().filter(author_id=self.request.user.id).order_by("id")
        )
        return queryset

    serializer_class = TagsSerializer
    # pagination_class = BasePageNumberPagination
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )  # доступ только после аутентификации и только владельцу записи в БД. Не работает для ListView
    ordering_fields = ["id", "name"]  # Specifying which fields may be ordered against
    ordering = ["id"]  # default ordering

    schema = AutoSchema(
        tags=["Tags"],
        component_name="Tags",
        operation_id_base="Tags",
    )

    # def create(self, request, *args, **kwargs):
    #     # request.data["author"] = request.user.pk
    #     return super().create(request, *args, **kwargs)

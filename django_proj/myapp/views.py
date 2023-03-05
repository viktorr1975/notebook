# from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Notes, Groups
from .serializers import NotesSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
# from .filters import ArticleFilterSet
from rest_framework.schemas.openapi import AutoSchema

from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, '_index.html', {
        'categories': Groups.objects.all()
        #'categories': Groups.objects.all().filter(author_id=3).order_by("id")
    })


def category_detail(request, group_id):
    category = get_object_or_404(Groups, id=group_id)
    return render(request, 'detail.html', {
        'category': category
    })


class AllNotesListView(ListView):
    """Представление для отображения списка всех заметок"""

    model = Notes
    context_object_name = "notes"
    template_name = "all_notes.html"

class NoteDetailView(DetailView):
    """Представление для отображения одной заметки."""

    model = Notes
    context_object_name = "notes"
    template_name = "note_detail.html"

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
        '''
        Выборка заметок для аутентифицированного пользователя. Для AnonimousUser:
        SELECT "myapp_notes"."id", "myapp_notes"."created", "myapp_notes"."modified", "myapp_notes"."title", "myapp_notes"."content", "myapp_notes"."author_id_id", "myapp_notes"."tag_id_id", "myapp_notes"."group_id_id" FROM "myapp_notes" WHERE "myapp_notes"."author_id_id" IS NULL
        '''
        queryset = Notes.objects.all().filter(author_id=self.request.user.id).order_by("id")
        return queryset
    # def get_queryset(self):
    #     queryset = Article.objects.all().filter(author=self.request.user).order_by("-id")
    #     return queryset
    serializer_class = NotesSerializer
    #pagination_class = BasePageNumberPagination
    # filterset_class = NotesFilterSet
    permission_classes = (IsAuthenticated, IsOwner)     #доступ только после аутентификации и только владельцу записи в БД. Не работает для ListView
    ordering_fields = ["id", "title"]  # Specifying which fields may be ordered against
    ordering = ["id"]  # default ordering

    schema = AutoSchema(
        tags=["Notes"],
        component_name="Notes",
        operation_id_base="Notes",
    )
    def create(self, request, *args, **kwargs):
        #request.data["author"] = request.user.pk
        return super().create(request, *args, **kwargs)
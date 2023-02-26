# from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Notes
from .serializers import NotesSerializer
from .pagination import BasePageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwner

# from .filters import ArticleFilterSet
from rest_framework.schemas.openapi import AutoSchema


# DRF
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
        queryset = Notes.objects.all().filter(author_id=self.request.user.id)
        return queryset
    # def get_queryset(self):
    #     queryset = Article.objects.all().filter(author=self.request.user).order_by("-id")
    #     return queryset
    serializer_class = NotesSerializer
    #pagination_class = BasePageNumberPagination
    # filterset_class = NotesFilterSet
    permission_classes = (IsAuthenticated, IsOwner)     #доступ только после аутентификации и только владельцу записи в БД. Не работает для ListView


    schema = AutoSchema(
        tags=["Notes"],
        component_name="Notes",
        operation_id_base="Notes",
    )
    def create(self, request, *args, **kwargs):
        #request.data["author"] = request.user.pk
        return super().create(request, *args, **kwargs)
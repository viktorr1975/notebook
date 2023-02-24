# from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Notes
from .serializers import NotesSerializer
from .pagination import BasePageNumberPagination

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
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    pagination_class = BasePageNumberPagination
    # filterset_class = NotesFilterSet

    schema = AutoSchema(
        tags=["Notes"],
        component_name="Notes",
        operation_id_base="Notes",
    )

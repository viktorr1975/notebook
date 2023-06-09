"""django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.schemas import get_schema_view
from myapp.views import (
    home,
    category_detail,
    tags_detail,
    edit_note_tags,
)  # AllTagsListView, TagDetailView   #AllNotesListView, NoteDetailView,

urlpatterns = [
    path("admin", admin.site.urls),  # все группы заметок пользователя
    #    path('', include('myapp.Django_urls', namespace="notes")),
    path("", home, name="home"),
    path(
        "category/<int:group_id>", category_detail, name="detail"
    ),  # все заметки пользователя
    path("tags", tags_detail, name="tags"),  # все тэги пользователя для данной заметки
    path(
        "note/<int:note_id>", edit_note_tags, name="edit_note_tags"
    ),  # добавляет/удаляем тэги к заметке пользователя
    #    path('accounts/login/', auth_views.LoginView.as_view()),        #set default  settings.LOGIN_URL
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # Add Django site authentication urls (for login, logout, password management)
    #    path("", AllNotesListView.as_view(), name="all-notes"),
    #    path("note/<int:pk>", NoteDetailView.as_view(), name="note-detail"),
    #     path("tags", AllTagsListView.as_view(), name="all-tags"),
    #     path("tag/<int:pk>", TagDetailView.as_view(), name="tag-detail"),
    path("api/", include("myapp.DRF_urls")),
    path(
        "api/drf-auth/", include("rest_framework.urls")
    ),  # добавим ссылки login/logout на страницах drf
    path(
        "openapi",
        get_schema_view(
            title="Notes", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

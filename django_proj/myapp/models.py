from django.db import models
#from django.conf import settings
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Tags(models.Model):
    """Тэги к заметкам."""
    name = models.CharField(max_length=16)

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Note {self.id}|{self.name}}"

class Notes(TimeStampedModel):
    """Таблица заметок"""
#    note = models.CharField(max_length=128)
    title = models.CharField(max_length=64)
    content = models.TextField()
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_notes", # имя, по которому через точку из объекта пользователя можно будет обратиться к списку его заметок
        help_text="Заметки пользователя",  # текст для человека
    )

    tag_id = models.ForeignKey(
        Tags,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tag",
        help_text="Тэг для заметки",  # текст для человека
    )
    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"Note {self.id}|{self.author_id}|{self.content}"

#    slug = AutoSlugField(populate_from='title')
#    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)

    # def slugify_function(self, content):
    #     return content.replace('_', '-').lower()

    # @property
    # def read_only_field(self):
    #     return getattr(self.author, "last_name", None)


# class Comment(models.Model):
#     """Комментарии к новости."""
#     coment = models.TextField()
#
#     to_article = models.ForeignKey(
#         to="articles.Article",
#         on_delete=models.CASCADE,
#         related_name="article_comments",
#     )
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="user_comments",
#     )
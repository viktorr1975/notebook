from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass


class Tags(models.Model):
    """Тэги к заметкам."""

    name = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        #        default=1,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_tags",
        # имя, по которому через точку из объекта пользователя можно будет обратиться к списку его заметок
        help_text="Тэги пользователя",  # текст для человека
    )

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"{self.id} | {self.name}"

    class Meta:
        """установка дополнительных параметров модели"""

        verbose_name_plural = "Tags"
        ordering = ["created"]


class Groups(models.Model):
    """Группы(типа папок) к заметкам. В принципе они аналогичны тэгам, но будут
    использоваться для иерархического группирования"""

    name = models.CharField(max_length=16)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        #        default=1,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_groups",
        # имя, по которому через точку из объекта пользователя можно будет обратиться к списку его групп
        help_text="Группы пользователя",  # текст для человека
    )

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"{self.id} | {self.name}"

    class Meta:
        """установка дополнительных параметров модели"""

        verbose_name_plural = "Groups"
        ordering = ["created"]


class Notes(TimeStampedModel):
    """Таблица заметок"""

    #    note = models.CharField(max_length=128)
    title = models.CharField(max_length=64)
    content = models.TextField()
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        #        default=1,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="user_notes",  # имя, по которому через точку из объекта пользователя можно будет обратиться к списку его заметок
        help_text="Заметки пользователя",  # текст для человека
    )
    # tag_id = models.ForeignKey(
    #     Tags,
    #     verbose_name='тэги пользователя',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="user_tags",
    #     help_text="Тэг для заметки",    # текст для человека
    # )
    tags = models.ManyToManyField(
        Tags,
        blank=True,
        null=True,  # для исключения сообщиения об обязательном значении в этом поле при добавлении заметки в админской панели.
        # даже при этих установках в таблице many-to-many полностью запись удаляется при удалении одной из связанных записей
        related_name="notes_by_tag",
        # имя, по которому через точку из объекта класса Tag можно будет обратиться к списку заметок
        help_text="Тэги заметок",  # текст для человека
    )
    group_id = models.ForeignKey(
        Groups,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notes_by_group",
        help_text="Название группы в которую входит заметка",  # текст для человека
    )

    def __str__(self):
        """переопределение строкового представления объекта."""
        return f"{self.id} | {self.author_id} | {self.content}"

    class Meta:
        """установка дополнительных параметров модели"""

        verbose_name_plural = "Notes"

    # @staticmethod
    # def get_products_by_id(ids):
    #     return Products.objects.filter(id__in=ids)
    #
    # @staticmethod
    # def get_all_products():
    #     return Products.objects.all()
    #
    # @staticmethod
    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return Products.objects.filter(category=category_id).order_by('-date')
    #     else:
    #         return Products.get_all_products()


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

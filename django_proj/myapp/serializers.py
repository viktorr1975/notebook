from rest_framework import serializers
from .models import Notes, Groups, Tags, CustomUser
from django.contrib.auth import get_user_model

# from drf_extra_fields.fields import Base64ImageField


class NonModelSerializer(serializers.Serializer):
    """Сериализатор с не-модельными полями."""


# class CommentSerializer(serializers.ModelSerializer):
#     """Сериализатор для модели Comment."""
#
#     class Meta:
#         model = Comment
#         # fields = "__all__"
#         exclude = ("author", "to_article",)


class NotesSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Notes."""

    # article_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # article_comments = CommentSerializer(many=True)
    # author = serializers.CharField(source='author.username', default=None)
    # author = UserSerializer()

    # image = Base64ImageField()
    author_id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # работает только на десериализацию(сохранение)

    # author_id = serializers.ReadOnlyField(source="author_id.username")      #при таком варианте надо ViewSet.create(): serializer.save(author_id=self.request.user)
    class Meta:
        model = Notes
        read_only_fields = ["id", "created", "modified"]
        fields = read_only_fields + [
            "title",
            "content",
            "author_id",
            "group_id",
            "tags",
        ]

        # fields = "__all__"
        # fields = ("id", "title", "content", "author")
        # exclude = []
        # fields = ("id", "title", "content", "article_comments", "author", "read_only_field", "slug", "image", "created", "modified", )

    def validate_group_id(
        self, value
    ):  # проверим, чтобы группа принадлежала пользователю (при сохранении вахно)
        if value:  # not None (JSON null)
            if (
                CustomUser.objects.all().filter(id=value.author_id_id)[0]
                != self.context["request"].user
            ):
                raise serializers.ValidationError("Группа пользователю не принадлежит")
        return value

    def validate_tags(
        self, value
    ):  # проверим, чтобы тэги принадлежали пользователю (при сохранении вахно)
        if value:  # not None (JSON null)
            for tag in value:
                if (
                    CustomUser.objects.all().filter(id=tag.author_id_id)[0]
                    != self.context["request"].user
                ):
                    raise serializers.ValidationError("Тэг пользователю не принадлежит")
        return value

    # def to_internal_value(self, data):
    #     # if self.context["request"]._request.method == "POST":
    #     #     # if not data.get("title"):
    #     #     #     data["title"] = "default_title"
    #     #     if not data.get("content"):
    #     #         data["content"] = "default_content"
    #     return super().to_internal_value(data)
    #
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     # representation["_request_data_method"] = self.context["request"]._request.method
    #     # representation["_request_data_url"] = self.context["request"]._request.path
    #     return representation

    # def create(self, validated_data):
    #     if not validated_data.get("author"):
    #         User = get_user_model()
    #         validated_data["author"] = User.objects.first()
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     # User = get_user_model()
    #     # author = User.objects.first()
    #     # new_comment = Comment(to_article=instance, author=author, coment="Изменено")
    #     # new_comment.save()
    #     return super().update(instance, validated_data)

    def validate(self, data):
        ...
        # if "Vinod" in data['author'].username:
        #     raise exceptions.ValidationError(detail="Vinod can not create post")  # NOQA
        return data


class GroupsSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Groups"""

    # group_notes = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all().filter(id=3), many=False) #не рабочее поле
    # article_comments = CommentSerializer(many=True)
    # author = serializers.CharField(source='author.username', default=None)
    # author = UserSerializer()

    author_id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # работает только на десериализацию(сохранение)

    # author_id = serializers.ReadOnlyField(source="author_id.username")      #при таком варианте надо ViewSet.create(): serializer.save(author_id=self.request.user)
    class Meta:
        model = Groups
        read_only_fields = ["id", "created"]
        fields = read_only_fields + ["name", "content", "author_id"]


class TagsSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Tags"""

    author_id = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # работает только на десериализацию(сохранение)

    # author_id = serializers.ReadOnlyField(source="author_id.username")      #при таком варианте надо ViewSet.create(): serializer.save(author_id=self.request.user)
    class Meta:
        model = Tags
        read_only_fields = ["id", "created"]
        fields = read_only_fields + ["name", "author_id"]

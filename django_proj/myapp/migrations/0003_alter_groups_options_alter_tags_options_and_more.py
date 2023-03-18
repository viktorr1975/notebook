# Generated by Django 4.1.6 on 2023-03-04 06:32

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_groups_author_id_tags_author_id_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="groups",
            options={"ordering": ["created"], "verbose_name_plural": "Groups"},
        ),
        migrations.AlterModelOptions(
            name="tags",
            options={"ordering": ["created"], "verbose_name_plural": "Tags"},
        ),
        migrations.RemoveField(
            model_name="notes",
            name="tag_id",
        ),
        migrations.AddField(
            model_name="groups",
            name="content",
            field=models.TextField(
                default=datetime.datetime(
                    2023, 3, 4, 6, 27, 10, 551573, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="groups",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="notes",
            name="tags",
            field=models.ManyToManyField(to="myapp.tags"),
        ),
        migrations.AddField(
            model_name="tags",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2023, 3, 4, 6, 32, 1, 896126, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
    ]

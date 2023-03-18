# Generated by Django 4.1.6 on 2023-03-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_alter_notes_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="group_id",
            field=models.ForeignKey(
                blank=True,
                help_text="Название группы в которую входит заметка",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="notes_by_group",
                to="myapp.groups",
            ),
        ),
    ]

# Generated by Django 3.2.13 on 2023-01-16 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0051_rename_group_application_workspace"),
    ]

    operations = [
        migrations.RenameField(
            model_name="template",
            old_name="group",
            new_name="workspace",
        ),
    ]

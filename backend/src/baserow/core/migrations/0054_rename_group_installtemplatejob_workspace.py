# Generated by Django 3.2.13 on 2023-01-16 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0053_rename_trashentry_group"),
    ]

    operations = [
        migrations.RenameField(
            model_name="installtemplatejob",
            old_name="group",
            new_name="workspace",
        ),
    ]

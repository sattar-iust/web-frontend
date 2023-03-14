# Generated by Django 3.2.13 on 2023-02-07 14:38

from django.db import migrations


def forward(apps, schema_editor):
    TrashEntry = apps.get_model("core", "TrashEntry")
    TrashEntry.objects.filter(trash_item_type="group").update(
        trash_item_type="workspace"
    )


def backward(apps, schema_editor):
    TrashEntry = apps.get_model("core", "TrashEntry")
    TrashEntry.objects.filter(trash_item_type="workspace").update(
        trash_item_type="group"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0055_auto_20230130_1118"),
    ]

    operations = [
        migrations.RunPython(forward, backward),
    ]

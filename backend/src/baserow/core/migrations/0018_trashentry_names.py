# Generated by Django 3.2.12 on 2022-05-02 16:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0017_alter_userprofile_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="trashentry",
            name="names",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(), null=True, size=None
            ),
        ),
    ]

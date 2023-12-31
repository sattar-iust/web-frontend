# Generated by Django 3.2.13 on 2023-01-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0039_settings_allow_global_group_creation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupinvitation",
            name="message",
            field=models.TextField(
                blank=True,
                help_text="An optional message that the invitor can provide. This will be visible to the receiver of the invitation.",
                max_length=250,
            ),
        ),
    ]

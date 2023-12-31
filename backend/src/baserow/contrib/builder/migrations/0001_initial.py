# Generated by Django 3.2.13 on 2023-02-03 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0042_add_ip_address_to_jobs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Builder",
            fields=[
                (
                    "application_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.application",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.application",),
        ),
    ]

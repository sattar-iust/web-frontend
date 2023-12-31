# Generated by Django 3.2.13 on 2023-02-22 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0064_rename_group_action_workspace"),
        ("database", "0110_alter_token_workspace"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airtableimportjob",
            name="workspace",
            field=models.ForeignKey(
                help_text="The workspace where the Airtable base must be imported into.",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.workspace",
            ),
        ),
    ]

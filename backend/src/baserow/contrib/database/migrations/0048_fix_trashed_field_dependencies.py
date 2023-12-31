# Generated by Django 3.2.6 on 2021-11-01 09:38
from django.db import migrations

# noinspection PyPep8Naming


def reverse(apps, schema_editor):
    pass


# noinspection PyPep8Naming
def forward(apps, schema_editor):
    FieldDependency = apps.get_model("database", "FieldDependency")
    trashed_dependencies_count, _ = FieldDependency.objects.filter(
        dependency__trashed=True
    ).delete()
    trashed_vias_count, _ = FieldDependency.objects.filter(via__trashed=True).delete()
    trashed_dependants_count, _ = FieldDependency.objects.filter(
        dependant__trashed=True
    ).delete()
    print(f"Fixed {trashed_dependants_count} trashed dependants")
    print(f"Fixed {trashed_vias_count} trashed vias")
    print(f"Fixed {trashed_dependencies_count} trashed dependencies")


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0047_fix_date_diff"),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]

# Generated by Django 3.2.6 on 2021-09-15 13:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0119_field_tsvector_column_created"),
    ]

    operations = [
        migrations.RunSQL(
            (
                """
CREATE OR REPLACE FUNCTION try_set_tsv(
    r regconfig, p_in text
)
RETURNS tsvector
AS
$$
BEGIN
    BEGIN
        RETURN to_tsvector(r, p_in);
    EXCEPTION WHEN others THEN
        BEGIN
            RETURN to_tsvector(r, left(p_in, 100000));
        EXCEPTION WHEN others THEN
            RETURN null;
        END;
    END;
END;
$$
LANGUAGE plpgsql;
"""
            ),
            "DROP FUNCTION IF EXISTS try_set_tsv(r regconfig, p_in text);",
        ),
    ]

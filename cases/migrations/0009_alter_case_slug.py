# Generated by Django 5.0.2 on 2024-02-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cases", "0008_rename_is_married_case_marriage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="slug",
            field=models.SlugField(max_length=40, unique=True),
        ),
    ]

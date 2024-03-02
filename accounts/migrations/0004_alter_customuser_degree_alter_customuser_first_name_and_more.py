# Generated by Django 5.0.2 on 2024-02-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_customuser_degree_alter_customuser_university"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="degree",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Basic Sciences", "Basic Sciences"),
                    ("Physiopathology", "Physiopathology"),
                    ("Medical Extern", "Medical Extern"),
                    ("Medical Intern", "Medical Intern"),
                    ("General Practicioner", "General Practicioner"),
                    ("Medical Resident", "Medical Resident"),
                    ("Medical Specialist", "Medical Specialist"),
                    ("Fellowship", "Fellowship"),
                    ("Superspecialist", "Superspecialist"),
                    (" ", "-None-"),
                ],
                help_text="Your current degree.",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
    ]
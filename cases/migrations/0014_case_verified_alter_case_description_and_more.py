# Generated by Django 5.0.2 on 2024-03-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cases", "0013_remove_case_date_of_admission_alter_case_dat_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="case",
            name="verified",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="case",
            name="description",
            field=models.CharField(
                blank=True,
                help_text="خلاصه\u200cای برای نشان دادن در صفحۀ اصلی که می\u200cتواند از عنوان طولانی\u200cتر باشد (تا دویست حرف).",
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="case",
            name="pretext",
            field=models.TextField(
                blank=True,
                help_text="اگر خواستید، می\u200cتوانید مقدمه\u200cای دربارۀ شرح\u200cحال خود بنویسید.",
                null=True,
            ),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-22 03:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Search",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "search_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="查詢時間"
                    ),
                ),
                ("project_id", models.TextField(verbose_name="項目名稱")),
                ("country_id", models.TextField(verbose_name="國家名稱")),
            ],
        ),
    ]

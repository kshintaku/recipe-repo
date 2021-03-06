# Generated by Django 3.1.1 on 2020-10-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="title")),
                ("recipe", models.JSONField(verbose_name="Recipe")),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
    ]

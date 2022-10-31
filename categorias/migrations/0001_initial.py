# Generated by Django 4.1.1 on 2022-10-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categorias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(default="DEFAULT VALUE", max_length=100)),
                (
                    "detalles",
                    models.CharField(default="DEFAULT VALUE", max_length=1000),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "Categorias",
            },
        ),
    ]

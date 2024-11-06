# Generated by Django 5.1.2 on 2024-11-02 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diabete_predict", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Consultation",
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
                ("date", models.DateField(auto_now_add=True)),
                ("tension", models.FloatField()),
                ("pull", models.FloatField()),
                ("masse", models.FloatField()),
                ("observation", models.TextField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="diabete_predict.patient",
                    ),
                ),
            ],
        ),
    ]
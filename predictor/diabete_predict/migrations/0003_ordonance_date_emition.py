# Generated by Django 5.1.2 on 2024-11-03 10:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diabete_predict", "0002_consultation"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordonance",
            name="date_emition",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]

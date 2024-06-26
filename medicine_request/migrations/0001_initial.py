# Generated by Django 5.0.6 on 2024-06-23 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Request",
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
                ("date_requested", models.DateTimeField(auto_now=True)),
                ("date_fulfilled", models.DateTimeField(null=True)),
                ("medicine", models.CharField(max_length=255)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "requester",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="patients.patient",
                    ),
                ),
            ],
        ),
    ]

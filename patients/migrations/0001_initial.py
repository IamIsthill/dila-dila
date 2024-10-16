# Generated by Django 5.1.1 on 2024-10-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("first_name", models.CharField(max_length=100, null=True)),
                ("middle_name", models.CharField(max_length=100, null=True)),
                ("last_name", models.CharField(max_length=100, null=True)),
                ("suffix", models.CharField(max_length=20, null=True)),
                ("sex", models.CharField(max_length=10, null=True)),
                ("blood_type", models.CharField(max_length=20, null=True)),
                ("DOB", models.DateField()),
                ("civil_status", models.CharField(max_length=20, null=True)),
                ("birth_place", models.CharField(max_length=100, null=True)),
                ("contact", models.BigIntegerField(null=True)),
                ("maiden_name", models.CharField(max_length=100, null=True)),
                ("address", models.CharField(max_length=255)),
                ("spouse_name", models.CharField(max_length=50, null=True)),
                ("mother_name", models.CharField(max_length=100, null=True)),
                ("family_member", models.CharField(max_length=20, null=True)),
                ("education", models.CharField(max_length=40, null=True)),
                ("employment_status", models.CharField(max_length=20, null=True)),
                ("is_nhts", models.BooleanField(default=True)),
                ("facility_household_no", models.IntegerField(null=True)),
                ("is_4ps", models.BooleanField(default=False)),
                ("household_no", models.IntegerField(null=True)),
                ("is_philhealth", models.BooleanField(default=False)),
                ("status_type", models.CharField(max_length=20, null=True)),
                ("philhealth_no", models.IntegerField(null=True)),
                ("member_category", models.CharField(max_length=50, null=True)),
                ("is_pcb", models.BooleanField(default=False)),
                ("added", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-added"],
            },
        ),
    ]

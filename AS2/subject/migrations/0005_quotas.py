# Generated by Django 4.1.1 on 2022-09-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subject", "0004_detail_section_detail_semester_detail_year"),
    ]

    operations = [
        migrations.CreateModel(
            name="quotas",
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
                ("sit", models.IntegerField()),
                (
                    "details",
                    models.ManyToManyField(
                        blank=True, related_name="qouta", to="subject.detail"
                    ),
                ),
            ],
        ),
    ]

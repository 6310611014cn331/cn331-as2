# Generated by Django 4.1.1 on 2022-09-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_user_quotas_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_quotas",
            name="amount_taken",
            field=models.IntegerField(max_length=1, null=True),
        ),
    ]
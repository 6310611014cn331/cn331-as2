# Generated by Django 4.1.1 on 2022-09-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
                ('teacher', models.CharField(max_length=64)),
                ('section', models.CharField(max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='detial',
        ),
    ]

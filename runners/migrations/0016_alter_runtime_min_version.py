# Generated by Django 4.2.1 on 2023-06-26 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runners', '0015_runtime_min_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtime',
            name='min_version',
            field=models.IntegerField(default=0),
        ),
    ]

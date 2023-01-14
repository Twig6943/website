# Generated by Django 2.2.12 on 2023-01-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0059_installerdraft'),
    ]

    operations = [
        migrations.AddField(
            model_name='installerdraft',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='installerdraft',
            name='reason',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='installerdraft',
            name='review',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='installerdraft',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]

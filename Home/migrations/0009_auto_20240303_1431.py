# Generated by Django 3.2.12 on 2024-03-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20240303_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='destination_status',
        ),
        migrations.RemoveField(
            model_name='container',
            name='source_status',
        ),
        migrations.AddField(
            model_name='container',
            name='collect_status',
            field=models.BooleanField(default='0'),
        ),
        migrations.AddField(
            model_name='container',
            name='drop_status',
            field=models.BooleanField(default='0'),
        ),
    ]

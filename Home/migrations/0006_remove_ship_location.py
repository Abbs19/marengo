# Generated by Django 3.2.12 on 2024-03-02 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_ship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship',
            name='location',
        ),
    ]
# Generated by Django 3.2.12 on 2024-03-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20240303_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='password',
            field=models.CharField(default='123456', max_length=50),
        ),
    ]
# Generated by Django 3.2.12 on 2024-03-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20240302_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]

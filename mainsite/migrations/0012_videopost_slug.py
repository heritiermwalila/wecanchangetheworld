# Generated by Django 2.2.1 on 2019-05-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_auto_20190524_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='videopost',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

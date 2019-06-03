# Generated by Django 2.2.1 on 2019-05-21 16:54

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('image_url', models.FileField(upload_to='static/images/%Y/%m/%d')),
                ('organisation', models.CharField(max_length=50)),
                ('title', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=4)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('expect', models.TextField(blank=True, verbose_name='Insert expect text')),
                ('description', ckeditor.fields.RichTextField()),
                ('status', models.CharField(choices=[('draft', 'draft'), ('published', 'published')], max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

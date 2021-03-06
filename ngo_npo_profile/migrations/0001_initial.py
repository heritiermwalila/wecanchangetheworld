# Generated by Django 2.2.1 on 2019-06-04 19:06

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Organisation name', max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('email', models.EmailField(blank=True, help_text='Organisation Email', max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('ceo', models.CharField(blank=True, max_length=50)),
                ('logo', models.FileField(default='static/images/noprofile.png', upload_to='ngo-npo/', verbose_name='Profile logo')),
                ('expect', models.TextField(blank=True, help_text='Expect text', max_length=255)),
                ('website_url', models.URLField(blank=True, help_text='website Address')),
                ('background_image', models.FileField(default='static/images/defaultbg.jpg', upload_to='ngo-npo/')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Organisation',
                'verbose_name_plural': 'Organisations',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo_npo_profile.Organisation')),
            ],
        ),
    ]

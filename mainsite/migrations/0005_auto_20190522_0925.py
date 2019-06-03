# Generated by Django 2.2.1 on 2019-05-22 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('ngo_npo_profile', '0002_auto_20190521_1940'),
        ('mainsite', '0004_auto_20190522_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opportunity',
            options={'verbose_name': 'Jobs', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='Opportunity by Company',
        ),
        migrations.RemoveField(
            model_name='opportunity',
            name='Opportunity by NGO or NPO',
        ),
        migrations.AddField(
            model_name='opportunity',
            name='company',
            field=models.ForeignKey(blank=True, help_text='Assign Opportunity to Company or leave blank', null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='ngo_or_npo',
            field=models.ForeignKey(blank=True, help_text='Assign Opportunity to NGO, NPO or leave blank', null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo_npo_profile.Organisation'),
        ),
    ]

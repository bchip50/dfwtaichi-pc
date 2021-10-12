# Generated by Django 3.2.7 on 2021-10-06 19:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('styles', '0010_alter_series_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='leaders',
            field=models.ManyToManyField(blank=True, help_text='Leaders for the series. Can administer this series.', related_name='leaders', through='styles.SeriesLeaders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='series',
            name='members',
            field=models.ManyToManyField(blank=True, help_text='Members of the series.', related_name='members', through='styles.SeriesMembers', to=settings.AUTH_USER_MODEL),
        ),
    ]

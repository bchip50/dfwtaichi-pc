# Generated by Django 3.0.11 on 2020-12-20 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='take_roll',
            field=models.BooleanField(default=False, verbose_name='Allow leader to take roll'),
        ),
    ]
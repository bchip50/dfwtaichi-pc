# Generated by Django 3.0.11 on 2020-12-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0002_series_take_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='wikipedia',
            field=models.URLField(blank=True, verbose_name='Reference page.'),
        ),
    ]

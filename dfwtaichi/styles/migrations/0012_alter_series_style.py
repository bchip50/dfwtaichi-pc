# Generated by Django 3.2.7 on 2021-12-22 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0011_auto_20211006_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seriesStyle', to='styles.style'),
        ),
    ]
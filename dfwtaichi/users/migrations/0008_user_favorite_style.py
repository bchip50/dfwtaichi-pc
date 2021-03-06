# Generated by Django 3.0.11 on 2020-12-25 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0004_auto_20201225_1051'),
        ('users', '0007_auto_20201222_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_style',
            field=models.ForeignKey(blank=True, help_text='Select your default TaiChi Style.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='styles.Style'),
        ),
    ]

# Generated by Django 3.0.11 on 2020-12-05 18:04

from django.db import migrations, models
import django_google_maps.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, help_text='Full name of the primary contact.', max_length=100, verbose_name='Name of the primary contact')),
                ('contact_email', models.EmailField(blank=True, max_length=254, verbose_name='Email address of the primary contact')),
                ('contact_phone', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Work phone number for the location')),
                ('gmaps_address', django_google_maps.fields.AddressField(blank=True, max_length=200)),
                ('gmaps_geolocation', django_google_maps.fields.GeoLocationField(blank=True, max_length=100)),
                ('title', models.CharField(help_text='Formal name for the location.', max_length=120, unique=True, verbose_name='Name of the location.')),
                ('address1', models.CharField(blank=True, max_length=120, verbose_name='Street Address line 1')),
                ('address2', models.CharField(blank=True, max_length=120, verbose_name='Street Address line 1')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='City')),
                ('state', models.CharField(default='Tx', max_length=2, verbose_name='State')),
                ('zipcode', models.CharField(blank=True, max_length=5, verbose_name='Zip code')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
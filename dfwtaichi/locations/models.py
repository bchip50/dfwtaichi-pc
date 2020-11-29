from django.db import models
from phone_field import PhoneField
from django_google_maps import fields as map_fields

class Loc_contact (models.Model):
    contact = models.CharField("Name of the primary contact", max_length=100, blank=True,
                               help_text="Full name of the primary contact.")
    contact_email = models.EmailField("Email address of the primary contact", blank=True)
    contact_phone = PhoneField("Work phone number for the location", blank=True)

    class Meta:
        abstract = True

class Gmaps(models.Model):
    gmaps_address = map_fields.AddressField(max_length=200, blank=True)
    gmaps_geoloc = map_fields.GeoLocationField(max_length=100, blank=True)

    class Meta:
        abstract = True

class Location(Loc_contact, Gmaps, models.Model):
    title = models.CharField("Name of the location.", max_length=120, unique=True,
                             help_text="Formal name for the location.")
    address1 = models.CharField("Street Address line 1", max_length=120, blank=True)
    address2 = models.CharField("Street Address line 1", max_length=120, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=2, default="Tx")
    zipcode = models.CharField("Zip code", max_length=5, blank=True)

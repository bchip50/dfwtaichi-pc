from django.contrib import admin

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField
from django.forms.widgets import TextInput

# Register your models here.
from dfwtaichi.locations.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "city",
        "contact",
        "contact_email",
        "contact_phone",
    ]
    formfield_overrides = {
        AddressField: {"widget": GoogleMapsAddressWidget},
        GeoLocationField: {"widget": TextInput},
    }

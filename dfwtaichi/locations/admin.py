from django.contrib import admin

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['title', 'address1', 'address2', 'city', 'state', 'zipcode',
                    'contact', 'contact-email', 'contact-phone',]
    formfield_overrides = {
        map_fields.AddressField: {'widget':
                                      map_widgets.GoogleMapsAddressWidget(attrs={
                                          'data-autocomplete-options': json.dumps({
                                              'types': ['geocode', 'establishment'],
                                              'componentRestrictions': {'country': 'us'}
                                          })
                                      })},
    }

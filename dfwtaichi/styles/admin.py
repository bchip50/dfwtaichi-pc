from django.contrib import admin

from dfwtaichi.styles.models import Style


@admin.register(Style)
class StylesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
    ]

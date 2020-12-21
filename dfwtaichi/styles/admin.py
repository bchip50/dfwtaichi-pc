from django.contrib import admin

from dfwtaichi.styles.models import Style, Series, Meeting


@admin.register(Style)
class StylesAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
    ]


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = [
        "style",
        "title",
        "slug",
    ]


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ["series", "day"]

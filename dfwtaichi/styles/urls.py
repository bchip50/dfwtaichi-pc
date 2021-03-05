from django.urls import path

from dfwtaichi.styles.views import style_detail_view, style_list_view

app_name = "styles"
urlpatterns = [
    path("<slug:slug>/", view=style_detail_view, name="detail"),
    path("", view=style_list_view, name="list"),
]

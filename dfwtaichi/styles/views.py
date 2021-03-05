from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Style


class StyleListView(ListView):
    model = Style


style_list_view = StyleListView.as_view()


class StyleDetailView(DetailView):
    model = Style


style_detail_view = StyleDetailView.as_view()

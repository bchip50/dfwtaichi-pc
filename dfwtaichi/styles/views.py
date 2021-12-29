from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Meeting, Series, Style


class StyleListView(ListView):
    model = Style


style_list_view = StyleListView.as_view()


class ActiveSeriesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = self.seriesStyle.all()
        return context


class StyleDetailView(ActiveSeriesMixin, DetailView):
    model = Style


style_detail_view = StyleDetailView.as_view()


class ActiveLeadersMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_leaders = Series.leaders.getrunfilter(active__eq=True)
        context["active_leaders"] = active_leaders
        return context


class SeriesDetailView(ActiveLeadersMixin, DetailView):
    model = Series


series_detail_view = SeriesDetailView.as_view()


class MeetingDetailView(DetailView):
    model = Meeting


meeting_detail_view = MeetingDetailView.as_view()

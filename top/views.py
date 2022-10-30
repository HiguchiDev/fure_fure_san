from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Choice
from django.db.models import Q
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    model = Choice
    queryset = Choice.objects.all()
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # dt_today = datetime.datetime.now()
        # today = dt_today.strftime('%Y/%m/%d') # 2022/##/##
        # ctx['today'] = today
        # ctx['join_date_today'] = dt_today.strftime('%Y%m%d') # 2022####
        # ctx['today_races'] = RaceInfo.objects.filter(date=today)
        return ctx
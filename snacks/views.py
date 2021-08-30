from django.db import models
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Snack
# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
class PathView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
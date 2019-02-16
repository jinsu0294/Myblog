from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from .models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark
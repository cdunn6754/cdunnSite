from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class TTTView(TemplateView):
    template_name = "ticTacToe/ttt.html"

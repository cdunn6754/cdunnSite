from django.urls import path

from .views import (TTTView, MinimaxApiView)

app_name='ticTacToe'

urlpatterns = [
    path('', TTTView.as_view(), name='ttt_view'),
    path("minimax-api/", MinimaxApiView.as_view(), name='minimax_api'),
]

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import JsonResponse
from ctypes import c_int, c_char_p, create_string_buffer

# Create your views here.
class TTTView(TemplateView):
    template_name = "ticTacToe/ttt.html"
    
    
class MinimaxApiView(View):
    def post(self, request):
        print(request.Post.get(board_array))
        
        return JsonResponse({'new_board':[1,2,3]})
        

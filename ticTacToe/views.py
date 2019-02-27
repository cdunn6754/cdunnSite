from django.shortcuts import render
import os
import time
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ctypes import cdll, c_int, c_char_p, c_char, create_string_buffer
import json

# Create your views here.
class TTTView(TemplateView):
    template_name = "ticTacToe/ttt.html"
    
    
@method_decorator(csrf_exempt, name='dispatch')
class MinimaxApiView(View):
    """
    An api for calling cpp minimax funcitonality for ttt ai
    """
        
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        next_move = self.get_next_move(
            ''.join(data.get("board_array")),
            data.get("agent_marker")
        )
        
        return JsonResponse({'next_move' : next_move})
        
    @staticmethod
    def get_next_move(board_array: str, agent_marker: str) -> int:
        """
        Calls the cpp so with the current board array and player char.
        The library returns the optimal index for the player to
        select next.
        """
        
        mm_lib = cdll.LoadLibrary(os.path.join(
            settings.BASE_DIR,
            "ticTacToe",
            "ttt_backend",
            "cpp",
            "libc_minimax_wrapper.so"
        ))
        # argument and return types for the minimax function exposed from
        # the library
        mm_lib.minimax.argtypes = [c_char_p, c_char]
        mm_lib.minimax.restypes = c_int
        
        c_board_array = create_string_buffer(board_array.encode('utf-8'))
        c_agent_marker = c_char(agent_marker.encode('utf-8'))
        # make it take a little longer
        time.sleep(1.5)
        return mm_lib.minimax(c_board_array, c_agent_marker)
        

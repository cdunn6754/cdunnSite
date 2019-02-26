from django.test import TestCase, Client
import json

from ticTacToe.views import MinimaxApiView

# Create your tests here.
class TestMinimax(TestCase):
    def setUp(self):
        self.c = Client()
        
    def test_minimax(self):
        """
        Should be able to give it an empty ttt board and get a
        response of 0 for the first entry and then 4
        """
        
        # empty board
        board = "EEEEEEEEE"
        res = MinimaxApiView.get_next_move(board, 'O')
        self.assertEqual(res, 0)
        board = "OEEEEEEEE"
        res = MinimaxApiView.get_next_move(board, 'X')
        self.assertEqual(res, 4)

    def test_request(self):
        """
        Hit the minimax api and make sure the whole thing works as expected.
        This is pretty much test_minimax but through a request
        """
        
        data = {
            "board_array": ["E" for x in range(9)],
            "agent_marker": "X"
        }
        response = self.c.post(
            '/tic-tac-toe/minimax-api/',
            json.dumps(data),
            content_type="application/json"
        )
        self.assertContains(response, 'next_move', count=1)
        self.assertEqual(response.json().get("next_move"), 0)
        
        data = {
            "board_array": ["X" if x==0 else "E" for x in range(9)],
            "agent_marker": "O"
        }
        response = self.c.post(
            '/tic-tac-toe/minimax-api/',
            json.dumps(data),
            content_type="application/json"
        )
        self.assertContains(response, 'next_move', count=1)
        self.assertEqual(response.json().get("next_move"), 4)

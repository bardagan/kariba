from KaribaPlayer import KaribaPlayer
import random

class BasicPlayer(KaribaPlayer):
    def __init__(self, name="Default Name"):
        super().__init__(name)
        
    def get_name(self):
        return self.name

    def get_move(self, board, cards_in_deck, hand, scores):   
        return hand[0], 1

class LowestCardPlayer(KaribaPlayer):
    def __init__(self, name="LowestCardPlayer"):
        super().__init__(name)
        
    def get_name(self):
        return self.name

    def get_move(self, board, cards_in_deck, hand, scores):  
        my_move = (hand[0], 1)  
        return my_move

class HighestCardPlayer(KaribaPlayer):
    def __init__(self, name="HighestCardPlayer"):
        super().__init__(name)
        
    def get_name(self):
        return self.name

    def get_move(self, board, cards_in_deck, hand, scores):
        my_move = (hand[-1], 1)
        return my_move

class GreedyPlayer(KaribaPlayer):
    def __init__(self, name="GreedyPlayer"):
        super().__init__(name)
        
    def get_name(self):
        return self.name

    def get_move(self, board, cards_in_deck, hand, scores):
        my_move = None
        for card in hand:
            if board[card - 1] >= 2:
                my_move = (card, 1)
        if my_move is None:
            my_move = (hand[-1], 1)
        return my_move

class GreedyPlayer2(KaribaPlayer):
    def __init__(self, name="GreedyPlayer2"):
        super().__init__(name)
        
    def get_name(self):
        return self.name

    def get_move(self, board, cards_in_deck, hand, scores):
        my_move = None
        for card in hand[::-1]:
            if board[card - 1] >= 2:
                my_move = (card, 1)
        if my_move is None:
            my_move = (hand[0], 1)
        return my_move


class RandomPlayer(KaribaPlayer):
    def __init__(self, name="RandomPlayer"):
        super().__init__(name)
        
    def get_name(self):
        return self.name

    def get_move(self, board, cards_in_deck, hand, scores):
        my_move = (random.choice(hand), 1)
        return my_move
        

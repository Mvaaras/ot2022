from random import shuffle
from entities.card import Card

class Board:
    """Board class keeps track of all the cards in the memory game

    Attributes:
        cards(array): a list of all the cards on the current board in random order
        size(int): the amount of pairs in the game
    """
    def __init__(self, size):
        """Constructor, creates a board of cards used in the memory game

        Args:
            size (int): The amount of pairs on the board
        """
        self.cards = []
        self.size = size
        for i in range(self.size):
            self.cards.append(Card(i+1))
            self.cards.append(Card(i+1))
        shuffle(self.cards)

    def open_card(self, card):
        """Opens a card on the board

        Args:
            card (int): The number of the card being opened

        Returns:
            Boolean: True, if the card was succesfully opened
        """
        if not self.cards[card].open:
            self.cards[card].open = True
            return self.cards[card].value
        return False

    def close_card(self, card):
        """Closes a card on the board

        Args:
            card (int): The number of the card being closed
        """
        self.cards[card].open = False

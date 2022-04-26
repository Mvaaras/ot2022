from random import shuffle


class Board:
    def __init__(self, size):
        self.cards = []
        self.size = size
        for i in range(self.size):
            self.cards.append(Card(i+1))
            self.cards.append(Card(i+1))
        shuffle(self.cards)

    def open_card(self, card):
        if not self.cards[card].open:
            self.cards[card].open = True
            return self.cards[card].value
        return False

    def close_card(self, card):
        self.cards[card].open = False


class Card:
    def __init__(self, value):
        self.value = value
        self.open = False


class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.players = 2
        self.turn = 1
        self.points = []
        self.not_closing = False
        self.saved = (-1, -1)
        for _ in range(self.players):
            self.points.append(0)

    def open_simple(self, card, end):
        card_value = self.board.open_card(card)
        if card_value:
            if end:
                self.not_closing = self.compare(card_value)
                self.turn = 3-self.turn
            else:
                self.saved = (card, card_value)
            return True
        return False

    def open_card(self, card, end):
        card_value = self.board.open_card(card)
        if card_value:
            if end:
                if not self.compare(card_value):
                    self.close_pair(card)
                self.turn = 3-self.turn
            else:
                self.saved = (card, card_value)
            return True
        return False

    def compare(self, card_value):
        if card_value == self.saved[1]:
            self.points[self.turn-1] += 1
            return True
        return False
    
    def end_game(self):
        if sum(self.points) == self.board.size:
            if self.points[0] > self.points[1]:
                return 1
            return 2
        return False

    def close_pair(self, card):
        if not self.not_closing:
            self.board.close_card(card)
            self.board.close_card(self.saved[0])

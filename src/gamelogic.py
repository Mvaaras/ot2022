from random import shuffle


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


class Card:
    """Class that represents a singular card in the memory game

    Attributes:
        value(int): the value of the card that is used to match it's pair
        open(boolean): wherer the card is open or closed 
    """
    def __init__(self, value):
        """Constructor for the card Class

        Args:
            value (int): The value of the card. There are 2 matching cards of each value on the board
        """
        self.value = value
        self.open = False


class Game:
    """Game class keeps track of all the logic in the memory game
    
    Attributes:
        board(Board): the game board associated with the game
        players(int): the amount of players in the game
        turn(int): used to keep track of the player turn
        points(array): keeps track of player points, [0] for player 1, [1] for player 2
        not_closing(boolean): keeps track of if the currently open pair will be closed or 
                            not after a delay. used to circumvent a situation with pygame
                            display updates
        saved(tuple): keeps track of the value and location of the last open card
                            used to check for pairs in the game logic
    """
    def __init__(self, size):
        """Constructor for the Game class

        Args:
            size (int): used to determine the size of the board
        """
        self.board = Board(size)
        self.players = 2
        self.turn = 1
        self.points = []
        self.not_closing = False
        self.saved = (-1, -1)
        for _ in range(self.players):
            self.points.append(0)

    def open_simple(self, card, end):
        """The method used for opening cards

        Args:
            card (int): Number of the card being opened
            end (bool): Wheter or not this card is the second card opened

        Returns:
            boolean: True if a card was successfully opened, false otherwise (if the card was already open)
        """
        card_value = self.board.open_card(card)
        if card_value:
            if end:
                self.not_closing = self.compare(card_value)
                self.turn = 3-self.turn #2 + 1 = 3, easily changes the turn between the two values
            else:
                self.saved = (card, card_value)
            return True
        return False

    def open_card(self, card, end):
        #disregard
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
        """Compares a card with the last saved card value

        Args:
            card_value (int): the value of the card being compared

        Returns:
            boolean: True if the compared card matches with the last saved card, False otherwise
        """
        if card_value == self.saved[1]:
            self.points[self.turn-1] += 1
            return True
        return False

    def end_game(self):
        """Checks to see if the game is over

        Returns:
            Int or boolean: The winning player number if the game has ended, False otherwise
        """
        if sum(self.points) == self.board.size:
            if self.points[0] > self.points[1]:
                return 1
            return 2
        return False

    def close_pair(self, card):
        """Closes the last 2 cards unless a pair was found

        Args:
            card (int): the location of the first card being closed
        """
        if not self.not_closing:
            self.board.close_card(card)
            self.board.close_card(self.saved[0])

class SinglePlayerGame(Game):
    def __init__(self, size):
        super().__init__(size)
        self.players = 1
        #in single player games, the first point slot (0) is used to track
        #the total number of turns taken to beat the game (for a score)

        #the second slot (1) is used to keep track of the found pairs so that end_game can be called
        #recycling!

    def open_simple(self, card, end):
        card_value = self.board.open_card(card)
        if card_value:
            if end:
                self.points[0] += 1
                self.not_closing = self.compare(card_value)
            else:
                self.saved = (card, card_value)
            return True
        return False

    def compare(self, card_value):
        if card_value == self.saved[1]:
            self.points[1] += 1
            return True
        return False

    def end_game(self):
        if self.points[1] == self.board.size:
            return True
        return False
from board import Board

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
            boolean: True if a card was successfully opened,
            False otherwise (if the card was already open)
        """
        card_value = self.board.open_card(card)
        if card_value:
            if end:
                self.not_closing = self.compare(card_value)
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
            boolean: True if the compared card matches with the last saved card,
            False otherwise
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

    """Single player version of the usual game logic. Most attributes are
    shared with the regular game logic class

    Changed attributes (refer to base class for the rest):
        turn(int): not used
        points(array): keeps track of player score, [0] for turns taken, [1] for
                    the total number of pairs opened so that end_game can be utilized
    """

    def __init__(self, size):
        super().__init__(size)
        self.players = 1

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

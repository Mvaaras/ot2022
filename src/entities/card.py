class Card:
    """Class that represents a singular card in the memory game

    Attributes:
        value(int): the value of the card that is used to match it's pair
        open(boolean): wherer the card is open or closed
    """
    def __init__(self, value):
        """Constructor for the card Class

        Args:
            value (int): The value of the card. There are 2 matching cards of
            each value on the board
        """
        self.value = value
        self.open = False

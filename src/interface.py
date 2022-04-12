import time
import os
import pygame
from gamelogic import Game

dirname = os.path.dirname(__file__)


class VisualCard(pygame.sprite.Sprite):

    def __init__(self, card, X, Y):
        super().__init__()
        self.card = card
        self.closed = pygame.image.load(
            os.path.join(dirname, "assets", "card_closed.png")
        )
        self.open = pygame.image.load(
            os.path.join(dirname, "assets", "card" +
                         str(self.card.value) + ".png")
        )

        self.image = self.closed

        self.rect = self.image.get_rect()

        self.rect.x = X
        self.rect.y = Y

    def update(self):
        if self.card.open:
            self.image = self.open
        else:
            self.image = self.closed


class VisualBoard:
    def __init__(self, board):
        self.board = board
        self.cards = []
        for i in range(len(board.cards)):
            self.cards.append(
                (
                    VisualCard(board.cards[i-1], 20+i *
                               40-40*(i % 2), 30+90*(i % 2)),
                    i-1
                )
            )


class Interface:
    
    wait_time = 1
    pygame.init()

    size = width, height = 640, 340

    game = Game(8)

    visual_board = VisualBoard(game.board)

    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    for card in visual_board.cards:
        all_sprites.add(card[0])

    all_sprites.draw(screen)

    end = False

    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                for card in visual_board.cards:
                    if card[0].rect.collidepoint(mouse_position[0], mouse_position[1]):
                        if game.open_simple(card[1], end):
                            card[0].update()
                            all_sprites.draw(screen)
                            pygame.display.update()
                            # the logic is currenlty here
                            # because I could not update the screen if I had it anywhere else
                            # this is very much a bandaid and I will
                            # be looking into ways to make this cleaner next week
                            if end:
                                time.sleep(wait_time)
                                game.close_pair(card[1])
                                for cards_update in visual_board.cards:
                                    cards_update[0].update()
                                all_sprites.draw(screen)
                                pygame.display.update()
                                end = False
                            else:
                                end = True

        all_sprites.draw(screen)
        pygame.display.update()

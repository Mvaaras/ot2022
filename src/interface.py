import time
import os
import pygame
import pygame.freetype
from gamelogic import Game, SinglePlayerGame

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

    pygame.init()
    size = width, height = 640, 340
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Memory")
    wait_time = 1
    #screen mode 0: start menu
    #screen mode 1: memory game
    #screen mode 2: win screen
    #screen mode 3: singleplayer memory game
    #screen mode 4: singleplayer win screen
    screen_mode = 0
    all_sprites = pygame.sprite.Group()
    font = pygame.freetype.Font(None, size=50, font_index=0, resolution=0, ucs4=False)

    game_menu = pygame.Rect(0, 0, 0, 0)
    gray = (55, 55, 55)

    pygame.display.update()

    while True:

        if screen_mode == 0:
            all_sprites.draw(screen)
            screen.fill((200,200,200))
            singleplayer_text = font.render("Singleplayer game", gray, bgcolor = (120, 120, 120))
            multiplayer_text = font.render("2 player game", gray, bgcolor = (120, 120, 120))
            screen.blit(singleplayer_text[0], (10, 110))
            screen.blit(multiplayer_text[0], (10, 180))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(str(multiplayer_text[1]))
                    mouse_position = pygame.mouse.get_pos()
                    if pygame.Rect(10, 110, singleplayer_text[1].width, singleplayer_text[1].height).collidepoint(mouse_position):
                        game = SinglePlayerGame(8)
                        visual_board = VisualBoard(game.board)
                        for card in visual_board.cards:
                            all_sprites.add(card[0])
                        all_sprites.draw(screen)
                        game_menu.update(0, 270, 640, 70)
                        end = False
                        screen_mode = 3
                    if pygame.Rect(10, 180, multiplayer_text[1].width, multiplayer_text[1].height).collidepoint(mouse_position):
                        game = Game(8)
                        visual_board = VisualBoard(game.board)
                        for card in visual_board.cards:
                            all_sprites.add(card[0])
                        all_sprites.draw(screen)
                        game_menu.update(0,270,640,70)
                        end = False
                        screen_mode = 1

        if screen_mode == 1:
            screen.fill((200, 200, 200))
            all_sprites.draw(screen)
            if game.turn == 1:
                scores_text1 = font.render("Player 1: " + str(game.points[0]),
                            (255, 255, 255),
                            bgcolor=(120, 120, 120))
                scores_text2 = font.render("Player 2: " + str(game.points[1]),
                            (255, 255, 255))
            else:
                scores_text1 = font.render("Player 1: " + str(game.points[0]),
                            (255, 255, 255))
                scores_text2 = font.render("Player 2: " + str(game.points[1]),
                            (255, 255, 255),
                            bgcolor=(120, 120, 120))

            pygame.draw.rect(screen, gray, game_menu)
            screen.blit(scores_text1[0], (5, 272))
            screen.blit(scores_text2[0], (310, 272))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
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
                                    if game.end_game():
                                        screen_mode = 2
                                else:
                                    end = True

        if screen_mode == 2:
            screen.fill((180,180,180))
            win_text = font.render("Player " + str(game.end_game()) + " wins", (0,0,0), bgcolor = (120,120,120))
            again_text = font.render("Click anywhere to return to menu", (0,0,0), size = 40)
            screen.blit(win_text[0], (40,150))
            screen.blit(again_text[0], (10,230))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = Game(8)
                    visual_board = VisualBoard(game.board)
                    for card in visual_board.cards:
                        all_sprites.add(card[0])
                    all_sprites.draw(screen)
                    game_menu.update(0,270,640,70)
                    end = False
                    screen_mode = 0

        if screen_mode == 3:
            screen.fill((200, 200, 200))
            all_sprites.draw(screen)
            if game.points[0] < 50:
                score = "Score: " + str(5000 - game.points[0]*100)
            else:
                score = "Score: 0"
            scores_text = font.render(score,
                                    (255, 255, 255),
                                    bgcolor = (120, 120, 120))

            pygame.draw.rect(screen,gray,game_menu)
            screen.blit(scores_text[0], (5,272))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    for card in visual_board.cards:
                        if card[0].rect.collidepoint(mouse_position[0], mouse_position[1]):
                            if game.open_simple(card[1], end):
                                card[0].update()
                                all_sprites.draw(screen)
                                pygame.display.update()
                                if end:
                                    time.sleep(wait_time)
                                    game.close_pair(card[1])
                                    for cards_update in visual_board.cards:
                                        cards_update[0].update()
                                    all_sprites.draw(screen)
                                    pygame.display.update()
                                    end = False
                                    if game.end_game():
                                        screen_mode = 4
                                else:
                                    end = True

        if screen_mode == 4:
            screen.fill((180, 180, 180))
            if game.points[0] <= 50:
                score = "Final score: " + str(5100 - game.points[0]*100)
            else:
                score = "Score: 0"
            win_text = font.render(score, (0,0,0), bgcolor = (120,120,120))
            again_text = font.render("Click anywhere to return to menu", (0, 0, 0), size=40)
            screen.blit(win_text[0], (40,150))
            screen.blit(again_text[0], (10,230))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game = Game(8)
                    visual_board = VisualBoard(game.board)
                    for card in visual_board.cards:
                        all_sprites.add(card[0])
                    all_sprites.draw(screen)
                    game_menu.update(0,270,640,70)
                    end = False
                    screen_mode = 0

import time
import os
import pygame
import pygame.freetype
from gamelogic import Game, SinglePlayerGame
from score_saving import ScoreSaving

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
    #screen mode 5: highscore screen
    screen_mode = 0
    saving = ScoreSaving()
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
            scoreboard_text = font.render("View highscore",
                                        gray, bgcolor = (120, 120, 120), size=30)
            screen.blit(singleplayer_text[0], (10, 110))
            screen.blit(multiplayer_text[0], (10, 180))
            screen.blit(scoreboard_text[0], (400, 300))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if pygame.Rect(10, 110, singleplayer_text[1].width,
                                singleplayer_text[1].height).collidepoint(mouse_position):
                        game = SinglePlayerGame(8)
                        visual_board = VisualBoard(game.board)
                        for card in visual_board.cards:
                            all_sprites.add(card[0])
                        all_sprites.draw(screen)
                        game_menu.update(0, 270, 640, 70)
                        end = False
                        screen_mode = 3
                    if pygame.Rect(10, 180, multiplayer_text[1].width,
                                multiplayer_text[1].height).collidepoint(mouse_position):
                        game = Game(8)
                        visual_board = VisualBoard(game.board)
                        for card in visual_board.cards:
                            all_sprites.add(card[0])
                        all_sprites.draw(screen)
                        game_menu.update(0,270,640,70)
                        end = False
                        screen_mode = 1
                    if pygame.Rect(400, 300, scoreboard_text[1].width,
                                scoreboard_text[1].height).collidepoint(mouse_position):
                        screen_mode = 5

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
                    break
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
                                        screen_mode = 2
                                else:
                                    end = True

        if screen_mode == 2:
            screen.fill((180,180,180))
            win_text = font.render("Player " + str(game.end_game()) +
                            " wins", (0,0,0), bgcolor = (120,120,120))
            again_text = font.render("Click anywhere to return to menu", (0,0,0), size = 40)
            screen.blit(win_text[0], (40,150))
            screen.blit(again_text[0], (10,230))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
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
                    break
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
                final_score = 5100 - game.points[0]*100
                saving.save_score(final_score)
                final_score_text = "Final score: " + str(final_score)
            else:
                score = "Score: 0"
            win_text = font.render(final_score_text, (0,0,0), bgcolor = (120,120,120))
            again_text = font.render("Click anywhere to return to menu", (0, 0, 0), size=40)
            screen.blit(win_text[0], (40,150))
            screen.blit(again_text[0], (10,230))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen_mode = 0

        if screen_mode == 5:
            screen.fill((180, 130, 180))
            saved_score = saving.read_score()

            if saved_score:
                score = "Your current highscore is " + str(saved_score)
            else:
                score = "You have not yet set a highscore"

            score_text = font.render(score, (0,0,0), size=30)
            again_text = font.render("Click anywhere to return to menu", (0, 0, 0), size=25)
            screen.blit(score_text[0], (40,150))
            screen.blit(again_text[0], (10,230))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen_mode = 0

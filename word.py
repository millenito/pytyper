import pygame
import random


class Word:
    def __init__(self, word, screen, game_font, color, bg_color):
        self.word = word
        self.screen = screen
        self.game_font = game_font
        self.color = color
        self.bg_color = bg_color
        self.screen_w, self.screen_h = pygame.display.get_surface().get_size()
        self.x = random.randint(0, self.screen_h - 300)
        self.y = random.randint(-1000, 0) * 3
        self.typed = False

    def draw(self):
        render = self.game_font.render(self.word, True, self.color)
        self.screen.blit(render, (self.x, self.y))

    def delete(self):
        self.typed = True
        self.color = self.bg_color

    def hit_bottom(self):
        return True if not self.typed and self.y >= self.screen_h - 165 else False

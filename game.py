import pygame
import sys
import random
from word import Word


class Game:
    def __init__(self, screen, mode):
        self.screen = screen
        self.mode = mode
        self.screen_w, self.screen_h = pygame.display.get_surface().get_size()
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)
        self.bg_color = pygame.Color('black')
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.words_list = ['oke', 'deh',
                           'katapanjang', 'kata', 'word', 'zyrex']
        self.words = []

    def gen_words(self):
        for i in range(50):
            rand_words = random.choice(self.words_list)
            self.words.append(Word(rand_words, self.screen,
                                   self.game_font, self.white, self.bg_color))

            self.words[i].draw()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.gen_words()

            # Blue Borders
            pygame.draw.rect(self.screen, self.blue, (0, self.screen_h - 170,
                                                      self.screen_w + 4, (self.screen_h - 300) + 4), 0)
            # Black box inside blue border
            pygame.draw.rect(self.screen, self.bg_color, (10, self.screen_h - 160,
                                                          self.screen_w - 20, self.screen_h - 300), 0)
            for w in self.words:
                w.y += 3
                if w.y >= self.screen_h - 165:
                    print('kena bawah')

            pygame.display.flip()  # Outputs to display
            clock.tick(60)  # Game tick 60 FPS

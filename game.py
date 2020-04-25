import pygame
import sys
import random
from random_words import RandomWords
from word import Word
import pygame_textinput


class Game:
    def __init__(self, screen, mode):
        self.screen = screen
        self.mode = mode
        self.screen_w, self.screen_h = pygame.display.get_surface().get_size()
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)
        self.bg_color = pygame.Color('black')
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.fall_speed = 1
        self.score = 0
        self.falling_words = []
        self.right = []

    def gen_words(self):
        rw = RandomWords()
        for i in range(50):
            rand_words = rw.random_word()
            while len(rand_words) > 10:
                rand_words = rw.random_word()

            self.falling_words.append(Word(rand_words, self.screen,
                                           self.game_font, self.white, self.bg_color))
            self.falling_words[i].draw()

    def draw(self):
        # Blue Borders
        pygame.draw.rect(self.screen, self.red, (0, self.screen_h - 170,
                                                 self.screen_w + 4, (self.screen_h - 300) + 4), 0)
        # Black box inside blue border
        pygame.draw.rect(self.screen, self.blue, (10, self.screen_h - 160,
                                                  self.screen_w - 20, self.screen_h - 300), 0)

        game_score = self.game_font.render(str(self.score), True, self.white)
        if self.score > 0:
            self.screen.blit(
                game_score, (self.screen_w - 95, self.screen_h - 140))

    def speedup(self, start_timer):
        current_time = pygame.time.get_ticks()
        seconds_passed = current_time - start_timer

        if seconds_passed >= 15000:
            self.fall_speed = 2
        elif seconds_passed >= 30000:
            self.fall_speed = 3
        elif seconds_passed >= 90000:
            self.fall_speed = 4
        elif seconds_passed >= 150000:
            self.fall_speed = 5

    def run(self):
        clock = pygame.time.Clock()
        start_timer = pygame.time.get_ticks()
        textbox = pygame_textinput.TextInput(antialias=True,
                                             text_color=self.white, cursor_color=self.white)
        textinput = ""

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.bg_color)

            if textbox.update(events):
                textinput = textbox.get_text()

                for w in self.falling_words:
                    if textinput == w.word and w.y > 0 and w.y < self.screen_h - 165:
                        self.score += 100
                        w.delete()
                        textbox.clear_text()
                        self.right.append(w.word)

            self.gen_words()
            self.draw()
            self.speedup(start_timer)

            # Draw textbox if there's no correct typed words or no text inputed
            if not textinput or self.right is not None:
                self.screen.blit(textbox.get_surface(),
                                 (25, self.screen_h - 145))

            for w in self.falling_words:
                w.y += self.fall_speed
                if w.hit_bottom():
                    print(w.word)
                    break

            pygame.display.flip()  # Outputs to display
            clock.tick(60)  # Game tick 60 FPS

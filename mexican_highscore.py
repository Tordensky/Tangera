import pygame
from pygame.locals import *
pygame.init()

class High_score_list():
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.filename = "highscorelist.dta"
        self.highscore_list = ["00:00:00"]
        self.font = pygame.font.SysFont("verdana", 30)

    def add_score(self, score):
        self.highscore_list.append(score)
        self.highscore_list.sort()

    def open_file(self):
        try:
            open_file = file(self.filename, 'r')
            line_list = []
            words_split = []
            line_list = open_file.readlines()
            for line in line_list:
                words_split = line.split()
                self.highscore_list.append(words_split[0])
        except IOError:
            pass

    def save_highscore(self):
        save_to_file = file(self.filename, 'w')
        self.highscore_list.sort()
        ##for score in self.highscore_list:
        save_to_file.write("%s \n" % (self.highscore_list[-1]))

    def draw(self, screen):
        tmp = self.font.render(self.highscore_list[-1], True, (255, 0, 0))
        screen.blit(tmp, (self.pos_x, self.pos_y))



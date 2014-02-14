import pygame
from pygame.locals import *
pygame.init()

class Drink_timer():
    def __init__(self, x, y, time=3, num=1):
        self.pos = (x, y)
        self.time_counter = 0.0
        self.milliseconds = 0.0
        self.seconds = 0
        self.minutes = time
        self.time_start = time
        self.num = num

        self.font = pygame.font.SysFont("verdana", 25)
        time = "%02d:%02d" % (self.minutes, self.seconds)
        self.timer = self.font.render(time, True, (200, 200, 200))

    def update(self, time_passed):
        self.milliseconds -= time_passed
        if self.milliseconds < 0:
            self.milliseconds = 99
            self.seconds -= 1
            if self.seconds < 0:
                self.seconds = 59
                self.minutes -= 1
                if self.minutes < 0:
                    pygame.event.post(pygame.event.Event(USEREVENT, num=self.num, text=""))
                    self.minutes += self.time_start
        time = "%02d:%02d" % (self.minutes, self.seconds)
        self.timer = self.font.render(time, True, (200, 200, 200))
    def get_time_string(self):
        return str("%02d:%02d:%02d" % (self.minutes, self.seconds, self.milliseconds))

    def draw(self, screen):
        screen.blit(self.timer, self.pos)


class Game_timer(Drink_timer):
    def __init__(self, x, y):
        Drink_timer.__init__(self, x,y)
        self.milliseconds = 0.0
        self.seconds = 0
        self.minutes = 0
        self.font = pygame.font.SysFont("verdana", 30)
        time = "%02d:%02d:%02d" % (self.minutes, self.seconds, self.milliseconds)
        self.timer = self.font.render(time, True, (200, 200, 200))

    def reset_timer(self):
        self.milliseconds = 0.0
        self.seconds = 0
        self.minutes = 0

    def update(self, time_passed):
        self.milliseconds += time_passed
        if self.milliseconds > 99:
            self.milliseconds = 0
            self.seconds += 1
            if self.seconds > 59:
                self.seconds = 0
                self.minutes += 1
                if self.minutes > 59:
                    self.minutes = 0
        time = "%02d:%02d:%02d" % (self.minutes, self.seconds, self.milliseconds)
        self.timer = self.font.render(time, True, (200, 200, 200))

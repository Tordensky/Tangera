import pygame
from pygame.locals import *
pygame.init()

class Button():
    def __init__(self, x, y, img, img_pressed, img_over, event, num=0, text="DEFAULT"):
        self.img = pygame.image.load(img).convert_alpha()
        self.img_pressed = pygame.image.load(img_pressed).convert_alpha()
        self.img_over = pygame.image.load(img_over).convert_alpha()
        self.pos = (x, y)
        self.sx = self.img.get_width()
        self.sy = self.img.get_height()
        self.rect = pygame.Rect(x, y, self.sx, self.sy)
        self.status = "none"
        self.event = pygame.event.Event(event, num=num, text=text)
        self.pressed = False
        self.timer = 5.0

    def update(self, time_passed_seconds):
        x, y = pygame.mouse.get_pos()
        ##a,b,c = pygame.mouse.get_pressed()
        ##self.timer += time_passed_seconds
        px, py = self.pos
        self.rect = pygame.Rect(px, py, self.sx, self.sy)
        if self.rect.collidepoint(x, y):
            if pygame.event.peek(MOUSEBUTTONDOWN):
                if not self.pressed:
                    pygame.event.post(self.event)
                    self.status = "pressed"
                    ##self.pressed = True
                    ##self.timer = 0.0

            else:
                self.status = "over"
                ##self.pressed = False

        else:
            self.status = "none"
            ##self.pressed = False

    def draw(self, x, y, screen):
        self.pos = (x, y)
        if self.status == "none":
            screen.blit(self.img, self.pos)
        elif self.status == "pressed":
            screen.blit(self.img_pressed, self.pos)
        elif self.status == "over":
            screen.blit(self.img_over, self.pos)

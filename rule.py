import button
import pygame
from button import *
from pygame.locals import *
pygame.init()

class Rule():
    def __init__(self, x, y, rule, id):
        ## info
        self.rule = rule
        self.id = id
        self.pos_x = x
        self.pos_y = y

        self.img = pygame.image.load("images/rule_bar.png").convert_alpha()

        self.font = pygame.font.SysFont("verdana", 14)
        self.print_rule = self.font.render(self.rule, True, (200, 200, 200))

        ## X button
        self.x_img = "images/x_button.png"
        self.x_img_over = "images/x_button_over.png"
        self.x_img_pressed = "images/x_button_pressed.png"
        self.x_button = Button(self.pos_x+6, self.pos_y+7, self.x_img, self.x_img_pressed, self.x_img_over, USEREVENT+5, num=self.id)

    def update(self, time_passed_seconds):
        self.x_button.update(time_passed_seconds)

    def draw(self, x, y, screen):
        self.pos_x = x
        self.pos_y = y
        screen.blit(self.img, (self.pos_x, self.pos_y))
        screen.blit(self.print_rule,(self.pos_x + 44, self.pos_y + 3))
        self.x_button.draw(x+7, y+7, screen)

class Rule_handler():
    def __init__(self, x, y):
        self.rules = []
        self.pos_x = x
        self.pos_y = y
        self.font = pygame.font.SysFont("verdana", 14)
        self.current_id = 0

    def add_new_rule(self, rule):
        self.rules.append(Rule(0,0,rule, self.current_id))
        self.current_id += 1

    def remove_rule(self, id):
        for rule in self.rules:
            if rule.id == id:
                self.rules.remove(rule)

    def remove_all_rules(self):
        self.rules = []

    def num_rules(self):
        return len(self.rules)

    def update(self, time_passed_seconds):
        for rule in self.rules:
            rule.update(time_passed_seconds)

    def draw(self, screen):
        pos_x = self.pos_x
        pos_y = self.pos_y
        num = 1

        for rule in self.rules:
            rule.draw(pos_x, pos_y, screen)
            screen.blit(self.font.render(str(str(num)+":"), True, (200, 200, 200)),(pos_x + 25, pos_y+3))
            num += 1
            pos_y += rule.img.get_height()-4

import pygame
from pygame.locals import *
pygame.init()

class Tangera_rules():
    def __init__(self, x, y):
        self.pos = (x, y)
        self.img = pygame.image.load("images/rules/intro.png").convert_alpha()

    def update(self, card, player):
        type_rule = card.value
        ## ALLE FAAR EN SLURK
        if type_rule == 1:
            print "kommer inn her"

            if card.kind < 3:
                self.img = pygame.image.load("images/rules/1.png").convert_alpha()
                player.total_bondskies += 1
                player.bondski = True
                return 0
            else:
                self.img = pygame.image.load("images/rules/skaal.png").convert_alpha()
                pygame.event.post(pygame.event.Event(USEREVENT+10, num=1))
                return 0

        ## SLURKER 2 -> 6 SORT = SELV / ROED = GI BORT
        if type_rule == 2:
            if card.kind < 3:
                self.img = pygame.image.load("images/rules/2_selv.png").convert_alpha()
                player.sips_given += 2
                return 0
            else:
                self.img = pygame.image.load("images/rules/2_bort.png").convert_alpha()
                return 2
        if type_rule == 3:
            if card.kind < 3:
                self.img = pygame.image.load("images/rules/3_selv.png").convert_alpha()
                player.sips_given += 3
                return 0
            else:
                self.img = pygame.image.load("images/rules/3_bort.png").convert_alpha()
                return 3
        if type_rule == 4:
            if card.kind < 3:
                self.img = pygame.image.load("images/rules/4_selv.png").convert_alpha()
                player.sips_given += 4
                return 0
            else:
                self.img = pygame.image.load("images/rules/4_bort.png").convert_alpha()
                return 4
        if type_rule == 5:
            if card.kind < 3:
                self.img = pygame.image.load("images/rules/5_selv.png").convert_alpha()
                player.sips_given += 5
                return 0
            else:
                self.img = pygame.image.load("images/rules/5_bort.png").convert_alpha()
                return 5
        if type_rule == 6:
            if card.kind < 3:
                self.img = pygame.image.load("images/rules/6_selv.png").convert_alpha()
                player.sips_given += 6
                return 0
            else:
                self.img = pygame.image.load("images/rules/6_bort.png").convert_alpha()
                return 6

        ## 7 GANGERN
        if type_rule == 7:
            self.img = pygame.image.load("images/rules/7.png").convert_alpha()
            return 3

        ## TEMA / ASSOSIASJONER
        if type_rule == 8:
            self.img = pygame.image.load("images/rules/tema.png").convert_alpha()
            return 3

        ## REGEL
        if type_rule == 9:
            ##pygame.event.post(pygame.event.Event(USEREVENT+3, num=0))
            self.img = pygame.image.load("images/rules/regel.png").convert_alpha()
            return 0

        ## GRIS
        if type_rule == 10:
            self.img = pygame.image.load("images/rules/gris.png").convert_alpha()
            return 3

        ## Suck and blow
        if type_rule == 11:
            self.img = pygame.image.load("images/rules/suck_and_blow.png").convert_alpha()
            return 3

        ## BUSSTUR
        if type_rule == 12:
            self.img = pygame.image.load("images/rules/buss_tur.png").convert_alpha()
            player.buss = True
            return 0

        ## MEXICAN WAVE
        if type_rule == 13:
            self.img = pygame.image.load("images/rules/mexican.png").convert_alpha()
            return 0

    def draw(self, screen):
        screen.blit(self.img, (self.pos))

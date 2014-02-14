import card_images
import card_dec
import pygame
from card_dec import *
from pygame.locals import *
pygame.init()

class Card_button():
    def __init__(self, x, y, card):
        self.scale = 0.25
        self.img = card.img
        self.img_back = pygame.image.load(card_images.red_back_image).convert_alpha()
        self.red_img = pygame.image.load("images/red_card.png").convert_alpha()
        self.green_img = pygame.image.load("images/green_card.png").convert_alpha()
        self.img = pygame.transform.scale(self.img,(int(self.img.get_width()*self.scale), int(self.img.get_height()*self.scale)))
        self.img_back = pygame.transform.scale(self.img_back,(int(self.img_back.get_width()*self.scale), int(self.img_back.get_height()*self.scale)))
        self.red_img = pygame.transform.scale(self.red_img,(int(self.red_img.get_width()*self.scale), int(self.red_img.get_height()*self.scale)))
        self.green_img = pygame.transform.scale(self.green_img,(int(self.green_img.get_width()*self.scale), int(self.green_img.get_height()*self.scale)))
        self.pos_x = x
        self.pos_y = y
        self.sx = self.img.get_width()
        self.sy = self.img.get_height()
        self.value = card.value

        self.is_pressed = False
        self.draw_red = False
        self.draw_green = False

    def new_card(self, card):
        self.img = card.img
        self.value = card.value
        self.img = pygame.transform.scale(self.img,(int(self.img.get_width()*self.scale), int(self.img.get_height()*self.scale)))
        self.is_pressed = False
        self.draw_red = False
        self.draw_green = False

    def get_status(self):
        if self.is_pressed:
            return self.value
        else:
            return 0

    def get_width(self):
        return self.sx

    def get_height(self):
        return self.sy

    def change_red_status(self):
        if self.draw_red:
            self.draw_red = False
        else:
            self.draw_red = True

    def change_green_status(self):
        if self.draw_green:
            self.draw_green = False
        else:
            self.draw_green = True

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.sx, self.sy)
        if self.rect.collidepoint(x, y):
            a,b,c = pygame.mouse.get_pressed()
            if a:
                self.is_pressed = True
            else:
                pass

    def draw(self, screen):
        ## card img
        if self.is_pressed:
            screen.blit(self.img, (self.pos_x, self.pos_y))
        elif not self.is_pressed:
            screen.blit(self.img_back, (self.pos_x, self.pos_y))

        ## color over img
        if self.draw_red:
            screen.blit(self.red_img, (self.pos_x, self.pos_y))
        if self.draw_green:
            screen.blit(self.green_img, (self.pos_x, self.pos_y))


class Strip():
    def __init__(self, x, y, num_cards, card_deck, drink_value, active, last=False):
        self.pos_x = x
        self.pos_y = y
        self.num_cards = num_cards
        self.drink_value = drink_value
        self.card_deck = card_deck
        self.cards = []

        ## Status
        self.last = last
        self.passed = False
        self.flipped = False
        self.active = active

        ## Distribute cards
        place_x = x
        place_y = y
        for n in range(num_cards):
            self.cards.append(Card_button(place_x, place_y, card_deck.get_next_card()))
            place_x += self.cards[0].get_width() + 4

        ## Calculate size
        self.width = len(self.cards)*(self.cards[0].get_width()+4)
        self.height = self.cards[0].get_height()

    ## RESET ALL CARDS
    def reset(self, active):
        self.passed = False
        self.flipped = False
        self.active = active
        for card in self.cards:
            if card.is_pressed:
                card.new_card(self.card_deck.get_next_card())

    def change_red_status(self):
        for card in self.cards:
            if card.is_pressed:
                card.change_red_status()
                break

    def change_green_status(self):
        for card in self.cards:
            if card.is_pressed:
                card.change_green_status()
                break

    ## UPDATE ROW
    def update(self):
        if self.active:
            for card in self.cards:
                if not self.flipped:
                    card.update()
                if card.get_status() > 0:
                    self.flipped = True
                    if card.get_status() >= 10:
                        return 2
                    elif card.get_status() == 1:
                        return 2
                    elif card.get_status() < 10:
                        return 1
                        self.passed = True

    ## DRAW ROW
    def draw(self, screen):
        ##if self.active and not self.flipped:
        ##    pygame.draw.rect(screen, (0,0,30), (self.pos_x-5, self.pos_y-5, self.width+5, self.height+5))
        for card in self.cards:
            card.draw(screen)

class Busstur():
    def __init__(self, x, y, rows):
        self.pos_x = x
        self.pos_y = y
        self.rows = rows
        self.strips = []
        self.card_deck = Card_deck(-100, -100, -100, -100)
        self.card_deck.add_new_deck()
        x_pos = x
        y_pos = y
        drink_value = 1
        num_cards = rows
        active = True
        self.complete = False
        self.draw_green = False

        for n in range(rows):
            if n == rows-1:
                self.strips.append(Strip(x_pos, y_pos, num_cards, self.card_deck, drink_value, active, True))
            else:
                self.strips.append(Strip(x_pos, y_pos, num_cards, self.card_deck, drink_value, active))
            y_pos -= (self.strips[0].height + 4)
            x_pos += int(self.strips[0].cards[0].get_height()/2)-4
            active = False
            drink_value += 1
            num_cards -= 1

        self.timer_one = 0.0
        self.timer_red_card = 0.0
        self.timer_green_card = 0.0

        self.given_sips = False
        self.num_sips = 0
        self.font = pygame.font.SysFont("verdana", 70)
        text = "%02d" % (self.num_sips)
        self.sips = self.font.render(text, True, (0, 0, 0))

    def reset(self):
        active = True
        for row in self.strips:
            row.reset(active)
            active = False
            self.given_sips = False

    def add_sips_to_player(self, player):
        player.sips_total += self.num_sips

    def update(self, time_passed_seconds):
        set_next = False
        self.draw_green = False
        for row in self.strips:
            value = row.update()

            if set_next:
                row.active = True
                set_next = False
            if value == 0:
                ## ikke snudd
                pass

            elif value == 1:
                ## Kort passert
                set_next = True
                if row.last:
                    self.complete = True
                    self.timer_green_card += time_passed_seconds
                    self.draw_green = True

                if self.draw_green:
                    row.change_green_status()
                    self.timer_green_card = 0.0

            elif value == 2:
                ## bildekort
                if not self.given_sips:
                    self.num_sips += row.drink_value
                    self.given_sips = True

                self.timer_one += time_passed_seconds
                self.timer_red_card += time_passed_seconds
                if self.timer_red_card > 0.05:
                    row.change_red_status()
                    self.timer_red_card = 0.0
                if self.timer_one > 1.0:
                    self.timer_one = 0.0
                    self.reset()



        if self.card_deck.cards_left() < self.rows+1:
            self.card_deck.add_new_deck()

    def draw(self, screen):
        text = "%02d" % (self.num_sips)
        self.sips = self.font.render(text, True, (0, 0, 0))
        screen.blit(self.sips, (580, 410))
        for row in self.strips:
            row.draw(screen)










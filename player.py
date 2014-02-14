import button
import pygame
from button import *
from pygame.locals import *
pygame.init()

class Player():
    def __init__(self, x, y, name, id):
        ## info
        self.name = name
        self.id = id
        print id
        ## Score updater
        self.score = 0
        self.sips_given = 0
        self.sips_total = 0
        self.sips_away_total = 0
        self.total_bondskies = 0

        self.promille = 0.0

        self.pos_x = x
        self.pos_y = y
        self.my_turn = False
        self.has_to_drink = False
        self.bondski = False
        self.buss = False
        self.text_num = 1
        self.drink_timer_draw = False

        ## player bar image
        self.img = pygame.image.load("images/player_bar.png").convert_alpha()

        ## player bar image my turn
        self.img_my_turn = pygame.image.load("images/player_bar_turn.png").convert_alpha()

        ## player bar has to drink
        self.img_has_drink = pygame.image.load("images/player_bar_yellow.png").convert_alpha()
        self.beer_mug_img = pygame.image.load("images/drink.png").convert_alpha()
        self.buss_img = pygame.image.load("images/buss.png").convert_alpha()

        ## bondski image
        self.glass_img = pygame.image.load("images/glass.png").convert_alpha()

        ## drink timer image
        self.drink_timer_img = pygame.image.load("images/timer.png").convert_alpha()

        self.font_max = pygame.font.SysFont("verdana", 25)
        self.font_large = pygame.font.SysFont("verdana", 16)
        self.font_small = pygame.font.SysFont("verdana", 14)
        self.print_name = self.font_large.render(self.name, True, (200, 200, 200))

        ## buttons
        ## X button
        self.x_img = "images/x_button.png"
        self.x_img_over = "images/x_button_over.png"
        self.x_img_pressed = "images/x_button_pressed.png"
        self.x_button = Button(self.pos_x+6, self.pos_y+7, self.x_img, self.x_img_pressed, self.x_img_over, USEREVENT+4, num=self.id)

        ## Pluss button
        self.pluss_img = "images/pluss_button.png"
        self.pluss_img_over = "images/pluss_button_over.png"
        self.pluss_img_pressed = "images/pluss_button_pressed.png"
        self.pluss_button = Button(self.pos_x+149, self.pos_y+9, self.pluss_img, self.pluss_img_pressed, self.pluss_img_over, USEREVENT+7, num=self.id)

        ## Minus button
        self.minus_img = "images/minus_button.png"
        self.minus_img_over = "images/minus_button_over.png"
        self.minus_img_pressed = "images/minus_button_pressed.png"
        self.minus_button = Button(self.pos_x+149, self.pos_y+22, self.minus_img, self.minus_img_pressed, self.minus_img_over, USEREVENT+8, num=self.id)

        ## All button
        self.all_img = "images/all_button.png"
        self.all_img_over = "images/all_button_over.png"
        self.all_img_pressed = "images/all_button_pressed.png"
        self.all_button = Button(self.pos_x+149, self.pos_y+35, self.all_img, self.all_img_pressed, self.all_img_over, USEREVENT+9, num=self.id)

    def update(self, time_passed_seconds):
        self.x_button.update(time_passed_seconds)
        self.pluss_button.update(time_passed_seconds)
        self.minus_button.update(time_passed_seconds)
        self.all_button.update(time_passed_seconds)
        ## TODO LAG EN TELLER SOM VEKSLER MELLOM DE FORSKJELLIGE STUSENE TIL SPILLEREN

    def text_update(self, num):
        self.text_num = num
        ## update promille
        ##if num == 3:


    def draw(self, x, y, screen):
        grams = (self.sips_total * 0.5)
        self.promille = grams/(70*0.65)
        self.pos_x = x
        self.pos_y = y
        if self.sips_given > 0:
            self.has_to_drink = True
        else:
            self.has_to_drink = False

        ## WHAT IMAGE PLAYER BAR TO BE BLITED
        if self.my_turn:
            screen.blit(self.img_my_turn, (self.pos_x, self.pos_y))
            if self.has_to_drink and not self.buss and not self.bondski:
                screen.blit(self.beer_mug_img, (self.pos_x +195, self.pos_y))
            if self.bondski:
                screen.blit(self.glass_img, (self.pos_x +195, self.pos_y))
        elif self.has_to_drink:
            screen.blit(self.img_has_drink, (self.pos_x, self.pos_y))
            screen.blit(self.beer_mug_img, (self.pos_x +195, self.pos_y))
        else:
            screen.blit(self.img, (self.pos_x, self.pos_y))

        ## EXTRA
        if self.drink_timer_draw and not self.bondski and not self.buss:
            screen.blit(self.drink_timer_img, (self.pos_x +195, self.pos_y))
        if self.buss:
            screen.blit(self.buss_img, (self.pos_x +150, self.pos_y-10))

        ## PLAYER NAME
        screen.blit(self.print_name,(self.pos_x + 17, self.pos_y + 3))
        if self.text_num == 1:
            ## TOTAL DRINKS RECIVED
            screen.blit(self.font_small.render(str("self: "+ str(self.sips_total)), True, (0, 150, 0)),(self.pos_x + 17, self.pos_y + 25))
            ## TOTAL DRINKS GIVEN AWAY
            screen.blit(self.font_small.render(str("away: "+ str(self.sips_away_total)), True, (150, 0, 0)),(self.pos_x + 80, self.pos_y + 25))
        if self.text_num == 2:
            ## TOTAL bondskies
            screen.blit(self.font_small.render(str("Bondskies: "+ str(self.total_bondskies)), True, (0, 150, 0)),(self.pos_x + 17, self.pos_y + 25))
        if self.text_num == 3:
            ## TOTAL bondskies
            prom = ("Promille: %0.2f") % (self.promille)
            screen.blit(self.font_small.render(prom, True, (0, 150, 0)),(self.pos_x + 17, self.pos_y + 25))

        ## CURRENT DRINKS RECIVED PRINTS ONLY IF MORE THAN ZERO
        if self.sips_given > 0:
            screen.blit(self.font_max.render(str(self.sips_given), True, (200, 200, 200)),(self.pos_x + 169, self.pos_y + 8))

        ## DRAW BUTTONS
        self.x_button.draw(x+7, y+7, screen)
        self.pluss_button.draw(x+149, y+5,screen)
        self.minus_button.draw(x+149, y+18, screen)
        self.all_button.draw(x+149, y+31, screen)

class Player_handler():
    def __init__(self, x, y):
        self.players = []
        self.pos_x = x
        self.pos_y = y
        self.current_id = 0
        self.current_player_num = -1
        self.current_text = 1

    def add_new_player(self, name):
        self.players.append(Player(0,0,name, self.current_id))
        self.current_id += 1

    def get_player_with_id(self, id):
        for player in self.players:
            if player.id == id:
                return player

    def goto_next_player(self):

        if len(self.players) > 1:
            if self.current_player_num+1 < len(self.players):
                self.current_player_num += 1
            else:
                self.current_player_num = 0

            self.players[self.current_player_num-1].my_turn = False
            self.players[self.current_player_num].my_turn = True
            return self.players[self.current_player_num]

        if len(self.players) == 1:
            self.players[0].my_turn = True
            return self.players[0]

        else:
            return 0

    def remove_player(self, id):
        ##print "kommer inn i remove player", id
        for player in self.players:
            if player.id == id:
                if player.my_turn == True:
                    self.players.remove(player)
                    self.current_player_num -= 1
                    ##self.goto_next_player()
                else:
                    index_num = self.players.index(player)
                    if index_num < self.current_player_num:
                        self.current_player_num -= 1
                    self.players.remove(player)
                break
        if self.current_player_num  < 0:
            self.current_player_num = 0
        ##print "spillere i listen",len(self.players)

    def get_current_player(self):
        for player in self.players:
            if player.my_turn:
                return player
        return 0

    def num_players(self):
        return len(self.players)

    def update(self, time_passed_seconds):
        for player in self.players:
            player.update(time_passed_seconds)

    def update_sips(self):
        for player in self.players:
            player.sips_total += player.sips_given
            player.bondski = False
            player.drink_timer_draw = False
            player.buss = False
            player.sips_given = 0

    def update_text_status(self):
        self.current_text += 1
        if self.current_text > 3:
            self.current_text = 1
        for player in self.players:
            player.text_num = self.current_text

    def draw(self, screen):
        pos_x = self.pos_x
        pos_y = self.pos_y
        for player in self.players:
            player.draw(pos_x, pos_y, screen)
            pos_y += player.img.get_height()-2




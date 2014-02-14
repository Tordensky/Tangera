background_image_filename = "images/Tangera.png"
import button
import pygame
import player
import inputbox
import rule
import card_dec
import drink_timer
import tangera_rules
import busstur
import mexican_highscore
from mexican_highscore import *
from busstur import *
from tangera_rules import *
from drink_timer import *
from card_dec import *
from rule import *
from inputbox import *
from player import *
from button import *
from pygame.locals import *
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

sound_on = True
## SOUNDS
mexican_wave_sound = pygame.mixer.Sound("sound/mexican.wav")
scratch = pygame.mixer.Sound("sound/scratch.wav")
judge = pygame.mixer.Sound("sound/judge.wav")
pig = pygame.mixer.Sound("sound/pig.wav")
bell = pygame.mixer.Sound("sound/bell.wav")
buss = pygame.mixer.Sound("sound/buss.wav")
everybody = pygame.mixer.Sound("sound/everybody.wav")
bom = pygame.mixer.Sound("sound/bom.wav")
casino = pygame.mixer.Sound("sound/casino.wav")
elvis = pygame.mixer.Sound("sound/elvis.wav")
double = pygame.mixer.Sound("sound/double.wav")
coin = pygame.mixer.Sound("sound/coin.wav")
regel = pygame.mixer.Sound("sound/regel.wav")

screen = screen_res = (1280, 800)

screen = pygame.display.set_mode((screen_res), FULLSCREEN, 32)
pygame.display.set_caption("Tangera")

background = pygame.image.load(background_image_filename).convert()
sips_to_give = 0

timer_on = True
mexican_timer_on = False
mexican_timer_active = False

big_font = pygame.font.SysFont("verdana", 70)
drink_timer = Drink_timer(950, 175, 3, 2)

highscore = High_score_list(325, 382)
highscore.open_file()
mexican_timer = Game_timer(325, 445)
mexican_button_start = Button(503, 390, "images/mexican_button_start.png", "images/mexican_button_start.png", "images/mexican_button_start_over.png", USEREVENT, 3)
mexican_button_stop = Button(503, 390, "images/mexican_button_stop.png", "images/mexican_button_stop.png", "images/mexican_button_stop_over.png", USEREVENT, 4)

time_passed_last_flip = 0.0
flip_allowed = False
## BUSSTUR HANDLER
busstur = Busstur(330, 430, 4)

class Dispatcher:
    def __init__(self):
        self.__handlers = {}

    def register_handler(self, etype, handler):
        # NB: This simple code assumes only a single handler
        # for each type
        self.__handlers[etype] = handler

    def dispatch(self, event):
        if event.type in self.__handlers:
            self.__handlers[event.type](event)
            print "eventen ligger i listen", event.type, pygame.event.event_name(event.type), event
        else:
            pass
            ##print "Unknown event type", event.type, pygame.event.event_name(event.type), event

def add_new_player(event):
    if player_handler.num_players() < 12:
        name = input_box(screen, background)
        player_handler.add_new_player(name)

def remove_player(event):
    if sound_on:
        elvis.set_volume(0.2)
        elvis.play()
    print event.num
    player_handler.remove_player(event.num)

def add_new_rule(event):
    if sound_on:
        regel.play()
    if rule_handler.num_rules() < 7:
        rule = rule_input_box(screen, background)
        rule_handler.add_new_rule(rule)

def remove_rule(event):
    rule_handler.remove_rule(event.num)

def sound_player(value):
    if sound_on:
        if value == 1:
            channel = everybody.play()
        elif value == 2:
            double.set_volume(0.2)
            ##double.play()
        elif value == 3:
            casino.set_volume(0.2)
            ##casino.play()
        elif value == 9:
            channel = judge.play()
        elif value == 10:
            pig.set_volume(0.5)
            pig.play()
        elif value == 11:
            bom.play()
        elif value == 12:
            buss.set_volume(0.5)
            buss.play()

def flip_next_card(event):
    ## reset busstur
    global flip_allowed
    if flip_allowed:
        pygame.mixer.fadeout(1000)

        if card_deck.get_current_value() == 12:
            global busstur
            busstur.add_sips_to_player(player_handler.get_current_player())
            busstur = Busstur(330, 430, 4)

        if player_handler.num_players() > 0:
            if card_deck.cards_left() > 0:
                card_deck.flip_next_card()
                player = player_handler.goto_next_player()
                player_handler.update_sips()
                global sips_to_give
                card = card_deck.get_current_card()
                sips_to_give = tangera_handler.update(card, player)

            else:
                card_deck.add_new_deck()
        ## Play card sound
        sound_player(card_deck.get_current_value())

        ## RESET MEXICAN WAVE
        global mexican_timer_on
        global mexican_timer_active
        global mexican_timer
        mexican_timer.reset_timer()
        mexican_timer.update(0.0)
        mexican_timer_on = False
        mexican_timer_active = False
        global time_passed_last_flip
        time_passed_last_flip = 0.0


def timer_next_card(time_passed_seconds):
    global time_passed_last_flip
    global flip_allowed
    time_passed_last_flip += time_passed_seconds
    if time_passed_last_flip < 0.2:
        flip_allowed = False
    else:
        flip_allowed = True


def add_sipp(event):
    player = player_handler.get_player_with_id(event.num)
    current_player = player_handler.get_current_player()
    if current_player == 0:
        return
    ## OBS LAG EN BEGRENSNING HER
    if sips_to_give > 0:
        if sound_on:
            coin.set_volume(0.2)
            coin.play()
        current_player.sips_away_total += 1
        player.sips_given += 1
        global sips_to_give
        sips_to_give -= 1

def give_all_sipp(event):
    global sips_to_give
    current_player = player_handler.get_current_player()
    if current_player == 0:
        return
    player = player_handler.get_player_with_id(event.num)
    player.sips_given += sips_to_give
    current_player.sips_away_total += sips_to_give
    sips_to_give = 0

def remove_sipp(event):
    player = player_handler.get_player_with_id(event.num)
    ## OBS LAG EN BEGRENSNING HER
    if player.sips_given > 0:
        current_player = player_handler.get_current_player()
        if current_player == 0:
            return
        current_player.sips_away_total -= 1
        player.sips_given -= 1
        global sips_to_give
        sips_to_give += 1

def give_all_players_sipp(event):
    for player in player_handler.players:
        player.sips_given += 1##event.num

def update_text_status(event):
    player_handler.update_text_status()

def timer_alarm(event):
        for player in player_handler.players:
            player.drink_timer_draw = True
        give_all_players_sipp(event)
        if sound_on:
            channel = bell.play()

def timer_on_off(event):
    global timer_on
    if timer_on:
        timer_on = False
    else:
        timer_on = True

def mexican_timer_start():
    if sound_on:
        global mexican_wave_sound
        channel = mexican_wave_sound.play()
    global mexican_timer_active
    mexican_timer_active = True

def mexican_timer_stop():
    if sound_on:
        global mexican_wave_sound
        scratch.set_volume(0.2)
        channel = scratch.play()
        channel = mexican_wave_sound.fadeout(200)
    global mexican_timer_active
    mexican_timer_active = False
    global highscore
    highscore.add_score(mexican_timer.get_time_string())

def event_handler(event):
    if event.num == 1:
        timer_on_off(event)
    elif event.num == 2:
        timer_alarm(event)
    elif event.num == 3:
        mexican_timer_start()
    elif event.num == 4:
        mexican_timer_stop()
    elif event.num == 5:
        add_new_player(event)



## ADD NEW PLAYER BUTTON
button = Button(68, 105, "images/new_player_button.png", "images/new_player_button_pressed.png", "images/new_player_button_over.png", USEREVENT, 5)

## ADD NEW RULE BUTTON
button2 = Button(305, 562, "images/new_rule_button.png", "images/new_rule_button_pressed.png", "images/new_rule_button_over.png", USEREVENT+3)

## NEXT CARD BUTTON
button3 = Button(1073, 273, "images/next_card_button.png", "images/next_card_button_pressed.png", "images/next_card_button_over.png", USEREVENT+6)

## TIMER BUTTON
timer_button = Button(950, 150, "images/timer_button.png", "images/timer_button_pressed.png", "images/timer_button_over.png", USEREVENT, 1)

## EVENT DISPATCHER
dispatcher = Dispatcher()

## UPDATE PLAYER TEXT
##dispatcher.register_handler(USEREVENT, update_text_status)
dispatcher.register_handler(USEREVENT, event_handler)

## FLIP CARD EVENT
dispatcher.register_handler(USEREVENT+1, flip_next_card)

## UPDATE PLAYER TEXT
dispatcher.register_handler(USEREVENT+2, update_text_status)

## ADD NEW RULE EVENT
dispatcher.register_handler(USEREVENT+3, add_new_rule)

## REMOVE PLAYER EVENT
dispatcher.register_handler(USEREVENT+4, remove_player)

## REMOVE RULE EVENT
dispatcher.register_handler(USEREVENT+5, remove_rule)

## NEXT CARD EVENT
dispatcher.register_handler(USEREVENT+6, flip_next_card)

## ADD SIPP TO PLAYER EVENT
dispatcher.register_handler(USEREVENT+7, add_sipp)

## REMOVE SIPP TO PLAYER EVENT
dispatcher.register_handler(USEREVENT+8, remove_sipp)

## GIVE ALL SIPPS TO PLAYER EVENT
dispatcher.register_handler(USEREVENT+9, give_all_sipp)

## GIVE ALL PLAYERS SIPPS EVENT
dispatcher.register_handler(USEREVENT+10, give_all_players_sipp)

## TIMER EVENT FOR CHANGING TEXT STATUS
##status_update = pygame.event.Event(USEREVENT, num=5)
pygame.time.set_timer(USEREVENT+2, 3500)

## CLASS FOR HANDLING OF PLAYERS
player_handler = Player_handler(44,134)

## CLASS FOR HANDLING OF RULES
rule_handler = Rule_handler(282, 583)

## TANGERA HANDLER
tangera_handler = Tangera_rules(277,226)

## GAME CARD DECK
card_deck = Card_deck(1076, 310, 1076, 531)
card_deck.add_new_deck()

clock = pygame.time.Clock()

##########################################
#########TEST TEST TEST TEST##############

##########################################


while 1:
        for event in pygame.event.get():
            key = pygame.key.get_pressed()

            if event.type == QUIT or key[pygame.K_ESCAPE]:
                highscore.save_highscore()
                exit()
            elif key[pygame.K_SPACE]:
                global flip_allowed
                if flip_allowed:
                    pygame.event.post(pygame.event.Event(USEREVENT+1, TEXT="SPACE" ))
                    flip_allowed = False
                    print "SPACE"
            elif key[pygame.K_r]:
                pygame.event.post(pygame.event.Event(USEREVENT+3))
            elif key[pygame.K_n]:
                pygame.event.post(pygame.event.Event(USEREVENT, num=5))
            elif key[pygame.K_t]:
                pygame.event.post(pygame.event.Event(USEREVENT+11))
            else:
                dispatcher.dispatch(event)

        time_passed = clock.tick(20) # limit to x FPS
        time_passed_seconds = time_passed / 1000.0   # convert to seconds
        timer_next_card(time_passed_seconds)
        ##print clock.get_fps()
        screen.blit(background, (0,0))
        card_deck.draw(screen)
        timer_button.update(time_passed_seconds)
        timer_button.draw(950,150,screen)
        button.update(time_passed_seconds)
        button.draw(68, 105,screen)
        button2.update(time_passed_seconds)
        button2.draw(305,562,screen)
        button3.update(time_passed_seconds)
        button3.draw(1073, 273,screen)
        tangera_handler.draw(screen)
        player_handler.update(time_passed_seconds)
        player_handler.draw(screen)

        rule_handler.update(time_passed_seconds)
        rule_handler.draw(screen)


        ## Drink timer
        if timer_on:
            drink_timer.update(time_passed/10)
        drink_timer.draw(screen)

        ## Timer for mexican wave
        if card_deck.get_current_value() == 13:
            highscore.draw(screen)
            if mexican_timer_active:
                mexican_timer.update(time_passed/10)
                mexican_button_stop.update(time_passed_seconds)
                mexican_button_stop.draw(503, 390, screen)
            elif not mexican_timer_active:
                mexican_button_start.update(time_passed_seconds)
                mexican_button_start.draw(503, 390, screen)
            mexican_timer.draw(screen)
        ##print mexican_timer.get_time_string()
        if card_deck.get_current_value() == 12:
            busstur.update(time_passed_seconds)
            busstur.draw(screen)


        ## PRINT SIPS LEFT
        left = big_font.render(str(sips_to_give), True, (150, 150, 150))
        screen.blit(left ,(330-int(left.get_width()/2),130))


        pygame.display.update()


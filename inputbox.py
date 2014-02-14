#! /usr/bin/python2
# -*- coding: latin_1 -*-
# i dette scriptet vil jeg prøve å ....

import pygame
from pygame.locals import *
pygame.init()

def input_box(screen, background):
    box_image = pygame.image.load("images/name_box.png").convert_alpha()
    input_name = ""
    font = pygame.font.SysFont("verdana", 34)
    print_name = font.render("", True, (200, 200, 200))
    num_char = 0
    while (1):
        event = pygame.event.poll()
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            new_key = event.key
            if new_key == K_BACKSPACE:
                input_name = input_name[:-1]
                if num_char != 0:
                    num_char -= 1

            elif new_key == K_RETURN:
                if num_char != 0:
                    break

            elif num_char >= 12:
                pass

            elif new_key == K_SPACE:
				input_name += str(" ")
				num_char += 1

            elif new_key <= 127:
                num_char += 1
                if new_key > 96:
                    input_name += str(chr(new_key-32))
                else:
                    input_name += str(chr(new_key))

        pos_x = int((screen.get_width()/2)-(box_image.get_width()/2))
        pos_y = int((screen.get_height()/2)-(box_image.get_height()/2))

        print_name = font.render(input_name, True, (200, 200, 200))
        screen.blit(box_image, (pos_x, pos_y))
        screen.blit(print_name, (pos_x + 68,pos_y + 83))
        pygame.display.update()

    return input_name

def rule_input_box(screen, background):
    box_image = pygame.image.load("images/rule_input_box.png").convert_alpha()
    input_name = ""
    font = pygame.font.SysFont("verdana", 20)
    print_name = font.render("", True, (200, 200, 200))
    num_char = 0
    while (1):
        event = pygame.event.poll()
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            new_key = event.key
            if new_key == K_BACKSPACE:
                input_name = input_name[:-1]
                if num_char != 0:
                    num_char -= 1

            elif new_key == K_RETURN:
                if num_char != 0:
                    break

            elif num_char >= 70:
                pass

            elif new_key == K_SPACE:
				input_name += str(" ")
				num_char += 1

            elif new_key <= 127:
                num_char += 1
                if new_key > 96:
                    input_name += str(chr(new_key-32))
                else:
                    input_name += str(chr(new_key))

        pos_x = int((screen.get_width()/2)-(box_image.get_width()/2))
        pos_y = int((screen.get_height()/2)-(box_image.get_height()/2))

        print_name = font.render(input_name, True, (200, 200, 200))
        screen.blit(box_image, (pos_x, pos_y))
        screen.blit(print_name, (pos_x + 50,pos_y + 91))
        pygame.display.update()

    return input_name

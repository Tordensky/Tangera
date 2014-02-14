import card_images
import pygame
import random
import pygame
from pygame.locals import *
pygame.init()

class Card():
    def __init__(self, image_filename, value, kind, name):
        self.img = pygame.image.load(image_filename).convert_alpha()
        self.value = value
        self.kind = kind
        self.name = name
        self.flipped = False

    def flip_card(self):
        self.flipped = True

class Card_deck():
    def __init__(self, x_flipped, y_flipped, x_deck, y_deck):
        self.pos_flipped = (x_flipped, y_flipped)
        self.pos_deck = (x_deck, y_deck)
        self.cards = []
        self.last_card_index = -1
        self.img_deck = pygame.image.load(card_images.red_back_image).convert_alpha()
        self.current_card = Card(card_images.red_back_image, 14, 5, "init card")

    def add_new_deck(self):
        self.cards = self.cards + [
        Card(card_images.ace_clubs_image, 1, 1, "Ace of Clubs"),
        Card(card_images.ace_spades_image, 1, 2, "Ace of Spades"),
        Card(card_images.ace_hearts_image, 1, 3, "Ace of Hearts"),
        Card(card_images.ace_diamond_image, 1, 4, "Ace of Diamonds"),
        Card(card_images.two_clubs_image, 2, 1, "Two of Clubs"),
        Card(card_images.two_spades_image, 2, 2, "Two of Spades"),
        Card(card_images.two_hearts_image, 2, 3, "Two of Hearts"),
        Card(card_images.two_diamond_image, 2, 4, "Two of Diamonds"),
        Card(card_images.tree_clubs_image, 3, 1, "Tree of Clubs"),
        Card(card_images.tree_spades_image, 3, 2, "Tre of Spades"),
        Card(card_images.tree_hearts_image, 3, 3, "Tree of Hearts"),
        Card(card_images.tree_diamond_image, 3, 4, "Tree of Diamonds"),
        Card(card_images.four_clubs_image, 4, 1, "Four of Clubs"),
        Card(card_images.four_spades_image, 4, 2, "Four of Spades"),
        Card(card_images.four_hearts_image, 4, 3, "Four of Hearts"),
        Card(card_images.four_diamond_image, 4, 4, "Four of Diamonds"),
        Card(card_images.five_clubs_image, 5, 1, "Five of Clubs"),
        Card(card_images.five_spades_image, 5, 2, "Five of Spades"),
        Card(card_images.five_hearts_image, 5, 3, "Five of Hearts"),
        Card(card_images.five_diamond_image, 5, 4, "Five of Diamonds"),
        Card(card_images.six_clubs_image, 6, 1, "Six of Clubs"),
        Card(card_images.six_spades_image, 6, 2, "Six of Spades"),
        Card(card_images.six_hearts_image, 6, 3, "Six of Hearts"),
        Card(card_images.six_diamond_image, 6, 4, "Six of Diamonds"),
        Card(card_images.seven_clubs_image, 7, 1, "Seven of Clubs"),
        Card(card_images.seven_spades_image, 7, 2, "Seven of Spades"),
        Card(card_images.seven_hearts_image, 7, 3, "Seven of Hearts"),
        Card(card_images.seven_diamond_image, 7, 4, "Seven of Diamonds"),
        Card(card_images.eight_clubs_image, 8, 1, "Eight of Clubs"),
        Card(card_images.eight_spades_image, 8, 2, "Eight of Spades"),
        Card(card_images.eight_hearts_image, 8, 3, "Eight of Hearts"),
        Card(card_images.eight_diamond_image, 8, 4, "Eight of Diamond"),
        Card(card_images.nine_clubs_image, 9, 1, "Nine of Clubs"),
        Card(card_images.nine_spades_image, 9, 2, "Nine of Spades"),
        Card(card_images.nine_hearts_image, 9, 3, "Nine of Hearts"),
        Card(card_images.nine_diamond_image, 9, 4, "Nine of Diamond"),
        Card(card_images.ten_clubs_image, 10, 1, "Ten of Clubs"),
        Card(card_images.ten_spades_image, 10, 2, "Ten of Spades"),
        Card(card_images.ten_hearts_image, 10, 3, "Ten of Hearts"),
        Card(card_images.ten_diamond_image, 10, 4, "Ten of Diamond"),
        Card(card_images.jack_clubs_image, 11, 1, "Jack of Clubs"),
        Card(card_images.jack_spades_image, 11, 2, "Jack of Spades"),
        Card(card_images.jack_hearts_image, 11, 3, "Jack of Hearts"),
        Card(card_images.jack_diamond_image, 11, 4, "Jack of Diamonds"),
        Card(card_images.queen_clubs_image, 12, 1, "Queen of Clubs"),
        Card(card_images.queen_spades_image, 12, 2, "Queen of Spades"),
        Card(card_images.queen_hearts_image, 12, 3, "Queen of Hearts"),
        Card(card_images.queen_diamond_image, 12, 4, "Queen of Diamonds"),
        Card(card_images.king_clubs_image, 13, 1, "King of Clubs"),
        Card(card_images.king_spades_image, 13, 2, "King of Spades"),
        Card(card_images.king_hearts_image, 13, 3, "King of Hearts"),
        Card(card_images.king_diamond_image, 13, 4, "King of Diamonds"),
        ]

    def cards_left(self):
        return len(self.cards)

    def get_current_card(self):
        return self.current_card

    def get_current_value(self):
        return self.current_card.value

    def flip_next_card(self):
        if len(self.cards) > 4:
            flip_index = self.last_card_index
            while flip_index == self.last_card_index:
                flip_index = random.randint(0, len(self.cards)-1)
            self.last_card_index = flip_index
            self.current_card = self.cards.pop(flip_index);
            self.current_card.flip_card()
            return self.current_card.value

        elif len(self.cards) > 0:
            flip_index = random.randint(0, len(self.cards)-1)
            self.current_card = self.cards.pop(flip_index);
            self.current_card.flip_card()
            return self.current_card.value

        else:
            return 0

    def get_next_card(self):
        if len(self.cards) > 4:
            flip_index = self.last_card_index
            while flip_index == self.last_card_index:
                flip_index = random.randint(0, len(self.cards)-1)
            self.last_card_index = flip_index
            self.current_card = self.cards.pop(flip_index);
            self.current_card.flip_card()
            return self.current_card

        elif len(self.cards) > 0:
            flip_index = random.randint(0, len(self.cards)-1)
            self.current_card = self.cards.pop(flip_index);
            self.current_card.flip_card()
            return self.current_card

        else:
            return 0

    def draw(self, screen):
        flipped_x, flipped_y = self.pos_flipped
        deck_x, deck_y = self.pos_deck
        pos_x = 0
        pos_y = 0
        num_cards = 0
        for card in self.cards:
            screen.blit(self.img_deck, (deck_x + pos_x, deck_y + pos_y))
            pos_x += 2
            pos_y += 2
            num_cards += 1
            if num_cards > 12:
                break
        screen.blit(self.current_card.img, (flipped_x, flipped_y))
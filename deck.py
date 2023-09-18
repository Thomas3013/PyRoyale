import pygame
import random
from cards import *
from unitclass import *


# placeholder remove when deck choosing is real
deck_chosen = '2.6'

if deck_chosen == '2.6':
    card0 = Unit(hog_rider, 0)
    card1 = Unit(ice_spirit, 0) #jasmine kelly
    card2 = Unit(ice_golem, 0)
    card3 = Unit(musketeer, 0)
    card4 = Unit(log, 0)
    card5 = Unit(fireball, 0)
    card6 = Unit(cannon, 0)
    card7 = Unit(skeletons, 0)

if deck_chosen == 'pekka':
    card0 = Unit(pekka, 0)
    card1 = Unit(bandit, 0)
    card2 = Unit(royal_ghost, 0)
    card3 = Unit(ewiz, 0)
    card4 = Unit(battle_ram, 0)
    card5 = Unit(poison, 0)
    card6 = Unit(zap, 0)
    card7 = Unit(minions, 0)

if deck_chosen == 'logbait':
    card0 = Unit(log, 0)
    card1 = Unit(goblin_barrel, 0)
    card2 = Unit(goblin_gang, 0)
    card3 = Unit(inferno_tower, 0)
    card4 = Unit(knight, 0)
    card5 = Unit(princess, 0)
    card6 = Unit(rocket, 0)
    card7 = Unit(ice_spirit, 0) # jasmine kelly

deck_size = 8
deck = [card0,card1,card2,card3,card4,card5,card6,card7]
random.shuffle(deck)
hand = deck[:4]
played_cards = []

def play_card(card_index):
    if card_index< len(hand):
        played_cards.append(hand.pop(card_index))

        if len(deck) > 0:
            hand.append(deck.pop(0))

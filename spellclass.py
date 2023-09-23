import pygame
import math
from tile import *
from pygame.locals import *
import math
from cards import *
from gblvars import *

class Spell:
    def __init__(self, spell, player):
        self.m_name = spell["name"]
        self.m_cost = spell["cost"]
        self.m_dmg = spell["dmg"]
        self.m_dmg_counter = spell["dmg_counter"]
        self.m_duration = spell["duration"]
        self.m_tower_dmg = spell["tower_dmg"]
        self.m_speed = spell["speed"]
        self.m_range = spell["range"]
        self.m_target = spell["target"]
        self.m_transport = spell["transport"]
        self.m_width = spell["width"]
        self.m_height = spell["height"]
        self.m_units = []
        self.m_kb = spell["kb"]
        self.m_ability = spell["ability"]
        self.m_colors = (spell["colors"])
        self.player = player
        self.id = SpellID.giveID()

    def get_color(self):
        return self.m_colors

    def get_elixir(self):
        return self.m_cost
    
    def get_name(self):
        return self.m_name
    
    def get_id(self):
        return self.id

    def get_tile_index(self, mouseX, mouseY):
        # mouseX = mouseX - 54
        mouseX = math.floor(mouseX / 24)
        print(mouseX)
        mouseY = math.floor(mouseY / 24)
        print(mouseY)
        tile = tiles[mouseY][mouseX]  # flipped?
        if tile == 1:

            return [(mouseX * 24), (mouseY * 24) - (self.m_height / 2)]
        else:
            print("invalid placement")
            return -1

    def spawn_spells(self, mouseX, mouseY):
        pos = self.get_tile_index(mouseX, mouseY)
        if (pos != -1):
            for x in range(self.m_count):
                self.m_units.append(pygame.Rect(pos[0] + (1.05 * x), pos[1] + (1.05 * x), self.m_width, self.m_height))
        return self.m_units

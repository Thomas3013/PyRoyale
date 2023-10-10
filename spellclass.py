import pygame
from tile import *
import math

class Spell:
    def __init__(self, spell, player):
        self.name = spell["name"]
        self.cost = spell["cost"]
        self.dmg = spell["dmg"]
        self.dmg_counter = spell["dmg_counter"]
        self.duration = spell["duration"]
        self.tower_dmg = spell["tower_dmg"]
        self.speed = spell["speed"]
        self.range = spell["range"]
        self.target = spell["target"]
        self.transport = spell["transport"]
        self.width = spell["width"]
        self.height = spell["height"]
        self.units = []
        self.kb = spell["kb"]
        self.ability = spell["ability"]
        self.colors = (spell["colors"])
        self.player = player
        #self.id = SpellID.giveID()

    def get_color(self):
        return self.colors

    def get_elixir(self):
        return self.cost
    
    def get_name(self):
        return self.name
    
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

            return [(mouseX * 24), (mouseY * 24) - (self.height / 2)]
        else:
            print("invalid placement")
            return -1

    def spawn_spells(self, mouseX, mouseY):
        pos = self.get_tile_index(mouseX, mouseY)
        if (pos != -1):
            for x in range(self.m_count):
                self.units.append(pygame.Rect(pos[0] + (1.05 * x), pos[1] + (1.05 * x), self.width, self.height))
        return self.units

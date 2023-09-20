import pygame
import math
from tile import *
from pygame.locals import *
import math
from cards import *
from gblvars import *

class Building:
    def __init__(self, build, player):
        self.m_name = build["name"]
        self.m_cost = build["cost"]
        self.m_hp = build["hp"]
        self.m_dmg = build["dmg"]
        self.m_splash = build["splash"]
        self.m_hit_speed = build["hit_speed"]
        self.m_lifetime = build["lifetime"]
        self.m_deploy_time = build["deploy_time"]
        self.m_range = build["range"]
        self.m_target = build["target"]
        self.m_width = build["width"]
        self.m_height = build["height"]
        self.m_units = []
        self.m_ability = build["ability"]
        self.m_colors = (build["colors"])
        self.player = player
        self.id = BuildID.giveID()

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

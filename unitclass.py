import pygame
from pygame.locals import *


class Unit:
    def __init__(self, troop, player):
        self.m_cost = troop["cost"]
        self.m_hp = troop["hp"]
        self.m_dmg = troop["dmg"]
        self.m_splash = troop["splash"]
        self.m_hit_speed = troop["hit_speed"]
        self.m_speed = troop["speed"]
        self.m_deploy_time = troop["deploy_time"]
        self.m_range = troop["range"]
        self.m_target = troop["target"]
        self.m_count = troop["count"]
        self.m_transport = troop["transport"]
        self.m_width = troop["width"]
        self.m_height = troop["height"]
        self.m_units = []
        self.m_colors = (troop["colors"])
        self.player = player

    def get_color(self):
        return self.m_colors

    def spawn_units(self, screen, mouseX, mouseY):
        for x in range(self.m_count):
            self.m_units.append(pygame.Rect(mouseX + (1.05 * x), mouseY + (1.05 * x), self.m_width, self.m_height))
        return self.m_units
    
    def get_elixir(self):
        return self.m_cost
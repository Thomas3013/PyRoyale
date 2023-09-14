import pygame
from pygame.locals import *


class Unit:
    def __init__(self, cost, hp, dmg, splash, hit_speed, speed, deploy_time, range, target, count, transport, height,
                 width, colors, player):
        self.m_cost = cost
        self.m_hp = hp
        self.m_dmg = dmg
        self.m_splash = splash
        self.m_hit_speed = hit_speed
        self.m_speed = speed
        self.m_deploy_time = deploy_time
        self.m_range = range
        self.m_target = target
        self.m_count = count
        self.m_transport = transport
        self.m_width = width
        self.m_height = height
        self.m_units = []
        self.m_colors = colors
        self.player = player

    def getColor(self):
        return self.m_colors

    def spawnUnits(self, screen, mouseX, mouseY):
        for x in range(self.m_count):
            self.m_units.append(pygame.Rect(mouseX + (1.05 * x), mouseY + (1.05 * x), self.m_width, self.m_height))
        return self.m_units

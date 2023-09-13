import pygame
from pygame.locals import *


class Unit:
    def __init__(self, cost, hit_speed, deploy_time, range, target, count, transport, height, width,colors):
        self.m_cost = cost
        self.m_hit_speed = hit_speed
        self.m_deploy_time = deploy_time
        self.m_range = range
        self.m_target = target
        self.m_count = count
        self.m_transport = transport
        self.m_width = width
        self.m_height = height
        self.m_units = []
        self.m_colors = colors

    def spawnList(self):
        for x in range(self.m_count):
            self.m_units.append(pygame.Rect(0,1, self.m_width, self.m_height))
    
    def spawnUnits(self, screen):
        for unit in self.m_units:
            print("helo")
            pygame.draw.rect(screen, self.m_colors, unit)
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
    def Movement(self):
        ##pygame  i dont get it
        ## every tick move pixels based off moveemnt speed + validate ground for gorunded unites
        return 0
    def attack(self):
        ##pygame 
        ##detect closest enemy based off range
        ## do self.damage * self.speed to it
        return 0
    def spawnList(self):
        for x in range(self.count):
            self.m_units.append(pygame.rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],self.m_width,self.m_height))
    def spawnUnits(self,screen):
        for i in range(self.m_count):
            pygame.draw.rect(screen,self.m_colors[i],self.m_units[i])

            
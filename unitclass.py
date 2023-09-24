import pygame
import math
from tile import *
from pygame.locals import *
import math
from cards import *
from gblvars import *


class AstarNode:
    def __init__(self, g, x, y):
        self.H = math.pow(x - 136, 2) + math.pow(y - 182,2)
        self.G = g
        self.F = self.G + self.H
        self.x = x
        self.y = y
        self.walkable = 0  # call wings function here

    def Hgetter(self):
        return self.H

    def Ggetter(self):
        return self.G

    def Fgetter(self):
        return self.F

    def Xgetter(self):
        return self.x

    def Ygetter(self):
        return self.y


class Unit:
    def __init__(self, troop, player):
        self.m_name = troop["name"]
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
        self.m_ability = troop["ability"]
        self.m_cc = troop["cc"]
        self.m_units = []
        self.m_colors = (troop["colors"])
        self.player = player
        self.id = UnitID.giveID()

    def get_color(self):
        return self.m_colors

    def get_elixir(self):
        return self.m_cost
    
    def get_name(self):
        return self.m_name
    
    def get_id(self):
        return self.id

    def get_tile_index(self, mouseX, mouseY):
        mouseX = mouseX - 54
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

    def spawn_units(self, mouseX, mouseY):
        pos = self.get_tile_index(mouseX, mouseY)
        if (pos != -1):
            for x in range(self.m_count):
                self.m_units.append(pygame.Rect(pos[0] + (1.05 * x), pos[1] + (1.05 * x), self.m_width, self.m_height))
        return self.m_units

    def aStarLeft(self, MouseX, MouseY):
        startNode = AstarNode(0, MouseX, MouseY)
        openlist = []
        closedlist = []
        openlist.append(startNode)
        currentNode = startNode
        pathed = False
        i = 0
        x = MouseX
        y = MouseY
        startX = startNode.Xgetter()
        startY = startNode.Ygetter()
        while (pathed is False):
            topleft = AstarNode((startX - x - 1) + (startY - y - 1), x - 1, y - 1)
            bottomleft = AstarNode((startX - x - 1) + (startY - y + 1), x - 1, y + 1)
            topright = AstarNode((startX - x + 1) + (startY - y - 1), x + 1, y - 1)
            bottomright = AstarNode((startX - x + 1) + (startY - y), x + 1, y)
            top = AstarNode((startX - x) + (startY - y - 1), x, y - 1)
            bottom = AstarNode((startX - x) + (startY - y + 1), x, y + 1)
            left = AstarNode((startX - x - 1) + (startY - y), x - 1, y)
            right = AstarNode((startX - x + 1) + (startY - y), x + 1, y)

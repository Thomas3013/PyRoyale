import pygame
from tile import *
import math
from gblvars import *
import heapq
import AstarAlgorithm
from AstarAlgorithm import Node, astar

class Unit:
    def __init__(self, troop, player):
        self.m_name = troop["name"]
        self.m_cost = troop["cost"]
        self.m_hp = troop["hp"]
        self.m_dmg = troop["dmg"]
        # self.m_splash = troop["splash"]
        self.m_hit_speed = troop["hit_speed"]
        self.m_speed = troop["speed"]
        self.m_deploy_time = troop["deploy_time"]
        self.m_range = troop["range"]
        self.m_target = troop["target"]
        self.m_count = troop["count"]
        self.m_transport = troop["transport"]
        self.m_width = troop["width"]
        self.m_height = troop["height"]
        # self.m_ability = troop["ability"]
        # self.m_cc = troop["cc"]
        self.m_units = None
        self.m_colors = (troop["colors"])
        self.player = player
        self.id = UnitID.giveID()
        self.placed = False
        self.x = None
        self.y = None
        self.get_tile_index(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.starting_node = AstarAlgorithm.Node(None,(self.x,self.y))
        self.path = get_path()
        # self.unit_rect_stats = pygame.Rect(self.x,self.y,self.m_width,self.m_height)

    def get_name(self):
        return self.m_name

    def set_name(self, name):
        self.m_name = name

    def get_cost(self):
        return self.m_cost

    def set_cost(self, cost):
        self.m_cost = cost

    def get_hp(self):
        return self.m_hp

    def set_hp(self, hp):
        self.m_hp = hp

    def get_dmg(self):
        return self.m_dmg

    def set_dmg(self, dmg):
        self.m_dmg = dmg

    def get_hit_speed(self):
        return self.m_hit_speed

    def set_hit_speed(self, hit_speed):
        self.m_hit_speed = hit_speed

    def get_speed(self):
        return self.m_speed

    def set_speed(self, speed):
        self.m_speed = speed

    def get_deploy_time(self):
        return self.m_deploy_time

    def set_deploy_time(self, deploy_time):
        self.m_deploy_time = deploy_time

    def get_range(self):
        return self.m_range

    def set_range(self, range):
        self.m_range = range

    def get_target(self):
        return self.m_target

    def set_target(self, target):
        self.m_target = target

    def get_count(self):
        return self.m_count

    def set_count(self, count):
        self.m_count = count

    def get_transport(self):
        return self.m_transport

    def set_transport(self, transport):
        self.m_transport = transport

    def get_width(self):
        return self.m_width

    def set_width(self, width):
        self.m_width = width

    def get_height(self):
        return self.m_height

    def set_height(self, height):
        self.m_height = height

    def get_color(self):
        return self.m_colors

    def get_ifDrawn(self):
        return self.placed

    def set_ifDrawn(self, placed):
        self.placed = placed

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return int(self.y)

    def set_y(self, y):
        self.y = y

    def get_path(self):
        if (self.x > )
            goal =
        astar()

    def get_tile_index(self, mouseX, mouseY):
        mouseX = mouseX - 54
        mouseX = math.floor(mouseX / 24)
        print(mouseX)
        mouseY = math.floor(mouseY / 24)
        print(mouseY)
        tile = tiles[mouseY][mouseX]  # flipped?
        if tile == 1:
            self.x = mouseX * 24
            self.y = (mouseY * 24) - (self.m_height / 2)
            return [int(mouseX * 24), int((mouseY * 24) - (self.m_height / 2))]
        if tile == 0:
            print("invalid placement")
            return -1
        if tile == 8:
            print("CASTLE")
            return -7

    def spawn_units(self, mouseX, mouseY, i):
        pos = self.get_tile_index(mouseX, mouseY)
        if pos != -1:
            self.m_units = (pygame.Rect(pos[0] + (1.05 * i), pos[1] + (1.05 * i), self.m_width, self.m_height))
        return self.m_units

    def movement(self):







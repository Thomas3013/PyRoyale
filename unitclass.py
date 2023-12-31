import pygame
from tile import *
import math
from gblvars import *
import AstarAlgorithm
import json


class Unit:
    def __init__(self, troop, player, x=None, y=None, path=None, client=None):
        self.troop = troop
        self.name = troop["name"]
        self.cost = troop["cost"]
        self.hp = troop["hp"]
        self.dmg = troop["dmg"]
        # self.m_splash = troop["splash"]
        self.hit_speed = troop["hit_speed"]
        self.speed = troop["speed"]
        self.deploy_time = troop["deploy_time"]
        self.range = troop["range"]
        self.target = troop["target"]
        self.count = troop["count"]
        self.transport = troop["transport"]
        self.width = troop["width"]
        self.height = troop["height"]
        # self.m_ability = troop["ability"]
        # self.m_cc = troop["cc"]
        self.units = None
        self.colors = (troop["colors"])
        self.player = player
        self.x = 0
        self.y = 0
        self.id = UnitID.giveID()
        self.placed = False
        if self.player != 1:
            self.get_tile_index(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            self.goal = self.goalFinder()
            # self.goal = (AstarAlgorithm.AstarNode(106, 101, 0, 0))
            self.home = AstarAlgorithm.AstarNode(self.x, self.y, self.goal.x, self.goal.y)
            self.path = AstarAlgorithm.Astar(self.home, self.goal.x, self.goal.y)
        else:
            self.x = x
            self.y = y
            self.path = path
        if client is not None:
            self.send_unit_json(client)

    def send_unit_json(self, client):
        dict_to_parse = {"troop": self.troop, "player": self.player, "x": self.x + 10, "y": self.y + 10,
                         "path": self.path}
        client.sendJson(dict_to_parse)

        # self.unit_rect_stats = pygame.Rect(self.x,self.y,self.m_width,self.m_height)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_dmg(self):
        return self.dmg

    def set_dmg(self, dmg):
        self.dmg = dmg

    def get_hit_speed(self):
        return self.hit_speed

    def set_hit_speed(self, hit_speed):
        self.hit_speed = hit_speed

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_deploy_time(self):
        return self.deploy_time

    def set_deploy_time(self, deploy_time):
        self.deploy_time = deploy_time

    def get_range(self):
        return self.range

    def set_range(self, range):
        self.range = range

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.count = count

    def get_transport(self):
        return self.transport

    def set_transport(self, transport):
        self.transport = transport

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_color(self):
        return self.colors

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

    def get_tile_index(self, mouseX, mouseY):
        mouseX = mouseX - 54
        mouseX = math.floor(mouseX / 10)
        # print(mouseX)
        mouseY = math.floor(mouseY / 10)
        # print(mouseY)
        tile = tiles[mouseY][mouseX]  # flipped?
        if tile == 0:
            self.x = (mouseX * 10) + 56
            self.y = (mouseY * 10) + 1
            print(self.x, "self x")
            print(self.y, "self y")
            return [int(mouseX * 10), int((mouseY * 10))]
        if tile == 1:
            # print("invalid placement")
            return -1
        if tile == 8:
            # print("CASTLE")
            return -7

    def goalFinder(self):
        if self.x > 266:
            return AstarAlgorithm.AstarNode(396, 171, 0, 0)
        else:
            return AstarAlgorithm.AstarNode(136, 171, 0, 0)

    def spawn_units(self, mouseX, mouseY, i):
        pos = self.get_tile_index(mouseX, mouseY)
        if pos != -1:
            self.units = (pygame.Rect(pos[0] + (1.05 * i), pos[1] + (1.05 * i), self.width, self.height))
        return self.units

    def movement(self):
        if len(self.path) > 0:
            self.x, self.y = self.path.pop()

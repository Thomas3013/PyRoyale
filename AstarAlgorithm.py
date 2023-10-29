import heapq
import walkable_xy_check
from tile import *
import math


class AstarNode:
    def __init__(self, x, y, goalx, goaly, parent=None):
        self.parent = parent
        self.x = x
        self.y = y
        if parent is not None:
            self.g = parent.g + 10
        else:
            self.g = 0

        self.h = abs(((goalx - x) + (goaly - y)) * 10)

        self.f = self.g + self.h

    def gAdjuster(self, new_parent):
        self.parent = new_parent
        self.g = new_parent.g + 10
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f


def Astar(Home, goalx, goaly) -> list:
    closed_hashmap = {}
    ope_list_queue = []
    ope_list_hashmap = {}
    # adding home to open list
    heapq.heappush(ope_list_queue, Home)
    currentNode = Home
    counter = 0
    print(Home.x, "home x")
    print(Home.y, "home y")

    # while goal tuple is not in closed list(closed_hashmap)
    while (goalx, goaly) not in closed_hashmap:
        counter += 1
        # print(counter)
        # getting lowest F cost square by popping ope_list_queue
        currentNode = heapq.heappop(ope_list_queue)
        # adding current node to closed list
        closed_hashmap[(currentNode.x, currentNode.y)] = currentNode
        # getting neighbors of currentNode
        temp_neighbors = neighbor_creator(currentNode, goalx, goaly)
        # for each neighbor that is walkable
        for neighbor in temp_neighbors:
            # if it is not in closed list(closed hashmap) else do skip it
            if (neighbor.x, neighbor.y) not in closed_hashmap:
                # if it isn't in open list heapush it to open list
                if (neighbor.x, neighbor.y) not in ope_list_hashmap:
                    heapq.heappush(ope_list_queue, neighbor)
                # if it is in open list and G cost is lower than open_list_hashmap's g value
                elif neighbor.G < ope_list_hashmap[(neighbor.x, neighbor.y)].G:
                    # redo g and f scores
                    ope_list_hashmap[(neighbor.x, neighbor.y)].gAdjuster(currentNode)
                    # reheap the ope_list_queue
                    heapq.heapify(ope_list_queue)

    return returHome(closed_hashmap[(goalx, goaly)], [], Home)


def returHome(paret, path, home):
    # print("return")
    if paret.x == home.x and paret.y == home.y:
        return path
    else:
        path.append((paret.x, paret.y))
        paret = paret.parent
        # print(paret.x)
        return returHome(paret, path, home)


def neighbor_creator(currentNode, goalx, goaly) -> list:
    neighbor_list = []
    neighbor_positions = [(-10, -10), (0, -10), (10, -10), (-10, 0), (10, 0), (-10, 10), (0, 10), (10, 10)]

    for dx, dy in neighbor_positions:
        x, y = currentNode.x + dx, currentNode.y + dy
        if get_tile_index(x, y):
            # print(x, "x", y, "y")
            neighbor_list.append(AstarNode(x, y, goalx, goaly, currentNode))
    # print("-------------------")

    return neighbor_list


def get_tile_index(nodeX, nodeY):
    nodeX = nodeX - 56

    if nodeX >= 429 or nodeX <= 0:
        return False
    if nodeY >= 769 or nodeY <= 0:
        return False

    nodeX = math.floor(nodeX / 10)
    nodeY = math.floor(nodeY / 10)

    tile = tiles[nodeY][nodeX]  # flipped?
    if tile == 0:
        x = (nodeX * 10) + 56
        y = (nodeY * 10) + 1
        return True
    if tile == 1:
        return False

import heapq
from unitindex import get_tile_index
import math
from tile import *


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # cost from start node to current node
        self.h = 0  # heuristic estimate from current node to goal node
        self.f = 0  # f = g + h

    def __lt__(self, other):
        return self.f < other.f


def astar(start, goal, get_neighbors):
    start_node = Node(None, start)
    goal_node = Node(None, goal)
    # start node - where unit placed
    # goal node - if unit on left or right side route them to left or right towers then to other tower

    open_list = []
    closed_set = set()
    # open list is nodes to be explored
    # closed list is nodes that have been explored and had their neighbors also explored

    heapq.heappush(open_list, start_node)
    # add start node to open queue

    while open_list:
        current_node = heapq.heappop(open_list)
        # current node is node with lowest f value form open list

        closed_set.add(current_node.position)
        # current node is marked as explored and sent to closed_set

        # check for node position
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
                # iterate through nodes and iterate their parents to get lowest F values in order and make a path
            return path[::-1]  # return the path in reverse order

        neighbors = get_neighbors(current_node)
        # generate neighbors

        for neighbor in neighbors:
            if (neighbor.position in closed_set) or (get_tile_index(neighbor.position[0],neighbor.position[1]) == -1):
                continue
            # check to make sure we are not double-checking nodes

            # Calculate the g, h, and f values for the neighbor node
            neighbor.g = current_node.g + 1  # Assuming each step has a cost of 1
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1]
            )
            neighbor.f = neighbor.g + neighbor.h
            # calculate F value for neighbors

            if any(neighbor.position == node.position and neighbor.f < node.f for node in open_list):
                continue
            # check if neighbor is in open list with a lower f value if so skip it

            # Add the neighbor to the open list
            heapq.heappush(open_list, neighbor)

    # if open list is empty and no path there is no way to get to the goal
    return None

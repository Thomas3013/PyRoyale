from tile import *
import math


def get_tile_index(mouseX, mouseY):
    mouseX = mouseX - 54
    mouseX = math.floor(mouseX / 24)
    print(mouseX)
    mouseY = math.floor(mouseY / 24)
    print(mouseY)
    tile = tiles[mouseY][mouseX]  # flipped?
    if tile == 1:
        return [int(mouseX * 24), int((mouseY * 24))]
    if tile == 0:
        print("invalid placement")
        return -1
    if tile == 8:
        print("CASTLE")
        return -7
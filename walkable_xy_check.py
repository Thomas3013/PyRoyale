from tile import *
import math


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
        print(x , y)
        return True
    if tile == 1:
        return False

def test_get_tile_index():
    # Define your grid or tiles here (assuming it's a 2D list)
    tiles = [
        [0, 1, 0],
        [0, 1, 1],
        [8, 0, 0]
    ]

    # Test cases with different node coordinates
    test_cases = [
        (70, 13000),  # Adjust these coordinates as needed
        (150, 50),
        (60, 160),
        # Add more test cases as needed
    ]

    for nodeX, nodeY in test_cases:
        result = get_tile_index(nodeX, nodeY)
        print(f"Node ({nodeX}, {nodeY}) -> Tile Index: {result}")



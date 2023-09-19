from single_linked_list import SingleLinkedList
from cards import *


class Player:
    def __init__(self):
        self.__elixir = 0
        self.__leftTower = 3200
        self.__rightTower = 3200
        self.__mainTower = 6000
        self.__playerDeckArray = []
        self.playerHand = {}
        self.setPlayerDeck()
        self.playerDeck = SingleLinkedList(None, self.__playerDeckArray)



    # Getter for elixir
    @property
    def elixir(self):
        return self.__elixir

    # Setter for elixir
    @elixir.setter
    def elixir(self, value):
        self.__elixir = value

    def setPlayerDeck(self):
        for i in range(6):
            self.__playerDeckArray.append(input("Enter a card name (e.g., unit::hog_rider):"))





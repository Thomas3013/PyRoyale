from single_linked_list import SingleLinkedList
from cards import *


class Player:
    def __init__(self):
        self.__elixir = 0
        self.__leftTower = 3200
        self.__rightTower = 3200
        self.__mainTower = 6000
        self.__playerDeckArray = []
        self.setPlayerDeck()
        self.playerDeck = SingleLinkedList()
        self.playerDeck.initializeDeck(self.__playerDeckArray)
        self.playerHand = self.playerDeck.initializeHand()
        self.pointer = self.playerDeck.next.next.next.next

    # Getter for elixir
    @property
    def elixir(self):
        return self.__elixir

    # Setter for elixir
    @elixir.setter
    def elixir(self, value):
        self.__elixir = value

    def setPlayerDeck(self):
        for i in range(8):
            self.__playerDeckArray.append(input("Enter a card name (e.g., unit::hog_rider):"))

    def cardUsed(self, card):
        while self.pointer is not None and self.playerHand[self.pointer] > 0:
            self.pointer = self.pointer.next
        self.playerHand[card] = 0

    def getHand(self):
        return self.playerHand

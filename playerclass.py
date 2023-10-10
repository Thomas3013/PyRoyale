import QuadTreeFile
from single_linked_list import SingleLinkedList
from QuadTreeFile import *
from cards import *
from unitclass import *

#loading images for cards
cardslot_images = []
for i in range(4):
    image = pygame.image.load(f'assets/card{i}.png')
    cardslot_images.append(image)
selected = pygame.image.load(f'assets/cardselect.png')

#coordinates for every card
cardCoords = [101, 209, 317, 425]


class Player:
    def __init__(self,player):
        self.playerNum = player
        self.elixer = 0
        self.leftTower = 3200
        self.rightTower = 3200
        self.mainTower = 6000
        self.playerDeckArray = []
        self.setPlayerDeck()
        self.playerDeck = SingleLinkedList()
        self.playerDeck.initializeDeck(self.playerDeckArray)
        self.playerHandKeys = self.playerDeck.initializeHand()
        self.playerHandArray = self.getHand()
        self.pointer = self.playerDeck.next.next.next.next

    # Getter for elixir
    @property
    def elixir(self):
        return self.elixer

    # Setter for elixir
    @elixir.setter
    def elixir(self, value):
        self.elixer = value

    def setPlayerDeck(self):
        self.playerDeckArray.append("unit::pekka")
        self.playerDeckArray.append("unit::hog_rider")
        self.playerDeckArray.append("unit::princess")
        self.playerDeckArray.append("unit::bandit")
        self.playerDeckArray.append("unit::royal_ghost")
        self.playerDeckArray.append("unit::ice_spirit")
        self.playerDeckArray.append("unit::goblin_gang")
        self.playerDeckArray.append("unit::knight")

        # for i in range(8):
        # self.__playerDeckArray.append(input("Enter a card name (e.g., unit::hog_rider):"))

    def cardUsed(self, card, position):
        while self.pointer.val in self.playerHandKeys:
            # checking if pointer value is in handkeys hashmap
            self.pointer = self.pointer.next
            if self.pointer.val not in self.playerHandKeys:
                break
        self.playerHandKeys[self.pointer.val] = 1
        if card in self.playerHandKeys:
            del self.playerHandKeys[card]
        self.playerHandArray[position] = self.pointer.val
        unitTree.insert(QuadTreeFile.Point(Unit(unit[card], self.playerNum)))

        #debug, ignore
        for val in self.playerHandArray:
            print(val)
        print(len(self.playerHandKeys))

    def getHand(self):
        keys = []
        for field, possible_values in self.playerHandKeys.items():
            keys.append(field)
        return keys
    
    # gets input from user and returns index of card selected ie: 0, 1, 2, 3
    def cardSelector(self, key):
        if 30 <= key <= 33:
            index = key - 30
            return index

    def displayCards(self,screen):
        screen.blit(cardslot_images[0],(cardCoords[0], 776))
        screen.blit(cardslot_images[1],(cardCoords[1], 776))
        screen.blit(cardslot_images[2],(cardCoords[2], 776))
        screen.blit(cardslot_images[3],(cardCoords[3], 776))
    # display update for cards and selected card    
    def displaySelected(self, screen, index):
        screen.blit(selected,(cardCoords[index]-4, 772))
        
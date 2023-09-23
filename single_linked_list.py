import random


class SingleLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pointer = None

    def initializeDeck(self, array):
        current = self
        random.shuffle(array)
        for i in range(len(array)):
            current.val = array[i]
            if i < len(array) - 1:
                current.next = SingleLinkedList()
                current = current.next
        current.next = self

    def initializeHand(self) -> dict:
        hand = {}
        current = self
        for i in range(4):
            hand[current.val] = 1
            current = current.next
        return hand

    # def printList(self, array):  # testing to print out list
    # current = self
    # for i in range(len(array) + 1):
    # print(current.val)
    # current = current.next

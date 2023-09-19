import Lib.random


class SingleLinkedList:
    def __init__(self, val=None, array=None):
        self.val = val
        self.next = None
        self.initializeDeck(array)


    def initializeDeck(self, array):
        current = self
        for i in range(len(array)):
            current.val = array[i]
            if i < len(array) - 1:
                current.next = SingleLinkedList()
                current = current.next
        current.next = self

    # def printList(self, array):  # testing to print out list
    # current = self
    # for i in range(len(array) + 1):
    # print(current.val)
    # current = current.next

    def randomizeDeck

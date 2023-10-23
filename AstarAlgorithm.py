import heapq

class AstarNode():
    def __init__(self,parent,x,y,goal):
        self.parent = parent
        self.g = parent.g + 10
        self.h = ((goal.x - x) + goal.y - y) * 10
        self.f = self.g + self.h
    def gAdjuster(self,new_parent):
        self.g = new_parent + 10
        self.f = self.g + self.h

def Astar(Home,Goal):
    found = False
    closed_list = {}
    open_list = []
    heapq.heappush(open_list, (Home.x, Home))
    while found is not True:
        currentNode = heapq.heappop(open_list)
        closed_list[currentNode] = currentNode
        open_list.push



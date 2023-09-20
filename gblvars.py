class gblvars:
    def __init__(self, int):
        self.num = int

    def giveID(self):
        self.num = self.num+1
        return self.num
    

UnitID = gblvars(0)
SpellID = gblvars(500)
BuildID = gblvars(1000)
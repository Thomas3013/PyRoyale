class gblvars:
    def __init__(self):
        self.num = 0

    def unitID(self):
        self.num = self.num+1
        return self.num
    

unitIDcounter = gblvars()
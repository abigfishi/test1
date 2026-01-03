class iinput(object):
    def __init__(self):
        self.s = ""
    def getstr(self):
        print('abc')
        self.s = input()
    def printstr(self):
        print(self.s.upper())
strobj=iinput()
strobj.getstr()
strobj.printstr()
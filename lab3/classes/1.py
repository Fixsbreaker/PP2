class SomeClass:
    def getString(self):
        self.string = str(input())

    def printString(self):
        print(self.string.upper())


cl = SomeClass()
cl.getString()
cl.printString()
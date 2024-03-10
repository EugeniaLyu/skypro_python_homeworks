class User:
    def __init__(self, first_name, last_name):
        self.imya = first_name
        self.familiya = last_name

    def printImya(self):
        print(self.imya)

    def printFamiliya(self):
        print(self.familiya)

    def printImyaFamiliya(self):
        print(self.imya, self.familiya)

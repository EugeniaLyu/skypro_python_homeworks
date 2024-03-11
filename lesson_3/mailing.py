class Mailing:
    to_address = "000000, г. , ул. , д. кв. "
    from_address = "000000, г. , ул. , д. кв. "
    cost = 0
    track = "XX000000000XX"

    def sayMailing(self):
        print(f'{self.to_address}, {self.from_address}, {self.cost}, {self.track}')

    def addAddress(self, address):
        self.address = address
    
    def getAddress(self):
        return self.address


class Address:
    index = "000000"
    city = "Unknown"
    street = "Unknown"
    house = "Unknown"
    room = "Unknown"

    def __init__(self, index, city, street, house, room):
        self.index = index
        self.city = city
        self. street = street
        self.house = house
        self.room = room

    def sayAddress(self):
        print(f'{self.index}, г. {self.city}, ул. {self.street}, д. {self.house}, кв. {self.room}')

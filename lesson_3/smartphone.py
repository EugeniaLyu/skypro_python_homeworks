class Smartphone:
    def __init__(self, brand, model, abonent_number):
        self.markaTelefona = brand
        self.modelTelefona = model
        self.abonentskiyNomer = abonent_number

    def sayUser(self):
        print(f"{self.markaTelefona} - {self.modelTelefona}. {self.abonentskiyNomer}")

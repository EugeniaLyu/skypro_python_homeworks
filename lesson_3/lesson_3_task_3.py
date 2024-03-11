from address import Address
from mailing import Mailing

message = Mailing()
message.sayMailing()
address = Address('628011', 'Ханты-Мансийск', 'Энгельса', '3', '11')
address2 = Address('167000', 'Сыктывкар', 'Первомайская', '123', '27')
message.addAddress(address)
message.getAddress()
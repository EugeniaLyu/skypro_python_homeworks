from address import Address
from mailing import Mailing

address1 = Address('628011', 'Ханты-Мансийск', 'Энгельса', '3', '11')
address2 = Address('167000', 'Сыктывкар', 'Первомайская', '123', '27')

message = Mailing(address1, address2, 1000, 'CA123456789UA')
print(f'Отправление {message.track} из {message.from_address.index}, г. {message.from_address.city}, ул. {message.from_address.street}, {message.from_address.house}-{message.from_address.room} в {message.to_address.index}, г. {message.to_address.city}, ул. {message.to_address.street}, {message.to_address.house}-{message.to_address.room}. Стоимость {message.cost} рублей.')

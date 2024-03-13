from smartphone import Smartphone
user1 = Smartphone("Apple", "11", "+79217850230")
user2 = Smartphone("Xiaomi", "Poco X4 Pro 5G", "+79112224792")
user3 = Smartphone("Samsung", "Galaxy A54 5G", "+79523385630")
user4 = Smartphone("Infinix", "Note 30 Pro(X678B)", "+79217850230")
user5 = Smartphone("Huawei", "Nova Y91(51097LTU)", "+79217850230")
catalog = []
catalog.append(user1)
catalog.append(user2)
catalog.append(user3)
catalog.append(user4)
catalog.append(user5)
for case in catalog:
    print(f'{case.brand} - {case.model}. {case.abonent_number}')

def bank():
  stavka = 0.1
  x = int(input("В каком размере будет вклад?"))
  y = int(input("На какой срок будет вклад?"))

  for z in range(y):
    x = x + (stavka * x)
    print("Сумма, которая будет на счету: ", x, "рублей за каждый год")
bank()

def month_to_season(num_month):
    if num_month == 12 or num_month == 1 or num_month == 2:
        print("Зима")
    elif num_month == 3 or num_month == 4 or num_month == 5:
        print("Весна")
    elif num_month == 6 or num_month == 7 or num_month == 8:
        print("Лето")
    elif num_month == 9 or num_month == 10 or num_month == 11:
        print("Осень")

month_to_season(int(input("Введи номер месяца: ")))

def is_year_leap(year):
    if year % 4 == 0:
        print("True")
    else: 
        print("False")

is_year_leap(int(input("Введите год: ")))
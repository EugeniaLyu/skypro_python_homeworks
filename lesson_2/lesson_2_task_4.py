def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0: 
        print("FizzBuzz")
    elif n % 3 == 0: 
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")

fizz_buzz(int(input("Введи число: ")))
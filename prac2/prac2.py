number = int(input("Введіть трицифрове число: "))
first_digit = number // 100
last_digit = number % 10


if first_digit == last_digit:
    print("Число є паліндромом") 
else:
    print("Число не є паліндромом") 
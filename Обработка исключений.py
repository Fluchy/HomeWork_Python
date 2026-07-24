try:
    a = float(input("Введите первое число\n"))
    b = float(input("Введите второе число\n"))
    result = a / b
    print("Результат деления первого числа на второе:", result)
except  ValueError:
    print("\nОшибка нечислового значания")
except ZeroDivisionError:
    print("\nОшибка деления на 0")
finally:
    print("\nProgram finished")
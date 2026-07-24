try:
    print("\n1- Сложение")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(num1 + num2)

    print("\n2- Вычитание")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(num1 - num2)

    print("\n3- Умножение")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(num1 * num2)

    print("\n4- Деление")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(num1 / num2)

except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Division by zero")


num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
action = input("Введіть дію (+, -, *, /): ")

if action == "+":
    print(num1 + num2)
elif action == "-":
    print(num1 - num2)
elif action == "*":
    print(num1 * num2)
elif action == "/":
    if num2 == 0:
        print("На нуль ділити не можна!")
    else:
        print(num1 / num2)
else:
    print("Невідома дія")

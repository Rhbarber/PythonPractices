text = "Ingresa el numero: "
number = input(text)
num = int(number)

while num != 0:
    if num > 0:
        if num % 2 == 1:
            print(f"{num} es impar.")
        else:
            print(f"{num} es par.")

    number = input(text)
    num = int(number)

print("Bye!")
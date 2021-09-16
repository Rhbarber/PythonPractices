value = 0
limit = 50000000

while value <= limit:
    diff = limit - value
    print("")
    print("Prueba Header")
    print(f"El valor es {value}")
    print(f"Faltan {diff} para llegar al limite.")
    value += 1
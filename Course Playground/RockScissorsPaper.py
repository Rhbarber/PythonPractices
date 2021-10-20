import random


# Funcion Principal
def main():
    showHeader()
    player = input("Inserta tu Nombre: ")
    game(player, "IA")


# Titulo/Header
def showHeader():
    print("-------------------------")
    print(" Piedra, Papel o Tijeras")
    print("-------------------------")


# Juego
def game(player1, player2):
    # Rondas & Victorias
    rounds = 3
    winsP1 = 0
    winsP2 = 0
    # Opciones
    rolls = ['piedra', 'papel', 'tijeras']

    # Sistema Mejor de 5
    while winsP1 < rounds and winsP2 < rounds:
        roll1 = getRoll(player1, rolls)
        roll2 = random.choice(rolls)  # IA Eleccion Random
        if not roll1:
            print("Intenta de Nuevo.")
            print()
            continue

        if roll2 not in rolls:
            print(f"Lo siento {player2}, {roll2} no es una jugada valida.")

        print(f"{player1} eligió {roll1}")
        print(f"{player2} eligió {roll2}")

        winner = winnerCheck(player1, player2, roll1, roll2)

        if winner is None:
            print("¡Esta ronda fue un empate!")
        else:
            print(f"El ganador de esta ronda es {winner}.")
            if winner == player1:
                winsP1 += 1
            elif winner == player2:
                winsP2 += 1

        print(f"Puntaje: {player1}: {winsP1} - {player2}: {winsP2}.")
        print()

    if winsP1 >= rounds:
        overallWinner = player1
    else:
        overallWinner = player2

    print(f"{overallWinner} gana el juego.")


# Ganador
def winnerCheck(player1, player2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("¡Empate!")
    elif roll1 == 'piedra':
        if roll2 == 'papel':
            winner = player2
        elif roll2 == 'tijeras':
            winner = player1
    elif roll1 == 'papel':
        if roll2 == 'tijeras':
            winner = player2
        elif roll2 == 'piedra':
            winner = player1
    elif roll1 == 'tijeras':
        if roll2 == 'piedra':
            winner = player2
        elif roll2 == 'papel':
            winner = player1
    return winner


# Obtener Decision
def getRoll(playerName, rolls):
    # Inputs y Conversiones
    print("Opciones Disponibles:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}. {r}")
        index += 1

    text = input(f"{playerName}, ¿Que número eliges? ")
    selectedIndex = int(text) - 1  # Esto debido al start = 1
    # roll = roll.lower().strip()  # Lower = Minusculas - Strip = Sin Espacios

    # Validar Jugadas
    if selectedIndex < 0 or selectedIndex >= len(rolls):  # len = returns the number of items (length) in an object.
        print(f'Lo siento {playerName}, "{text}" esta fuera de los Limites.')
        # Las comillas se pueden incluir en strings si los delimitadores no son el mismo tipo de comillas.
        return None
    return rolls[selectedIndex]  # Seleccionar de la lista


main()

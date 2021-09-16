import random

rolls = {
    'piedra': {
        'vence': ['tijeras'],
        'vencido': ['papel']
    },
    'papel': {
        'vence': ['piedra'],
        'vencido': ['tijeras']
    },
    'tijeras': {
        'vence': ['papel'],
        'vencido': ['piedra']
    },
}


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
    wins = {player1: 0, player2: 0}

    # Opciones
    rolls_names = list(rolls.keys())

    # Sistema Mejor de 5
    while not findWinner(wins, wins.keys()):
        roll1 = getRoll(player1, rolls_names)
        roll2 = random.choice(rolls_names)  # IA Eleccion Random
        if not roll1:
            print("Intenta de Nuevo.")
            print()
            continue

        print(f"{player1} eligió {roll1}")
        print(f"{player2} eligió {roll2}")

        winner = winnerCheck(player1, player2, roll1, roll2)

        if winner is None:
            print("¡Esta ronda fue un empate!")
        else:
            print(f"El ganador de esta ronda es {winner}.")
            wins[winner] += 1

        #print(f"Idk {wins}")
        print(f"Puntaje: {player1}: {wins[player1]} - {player2}: {wins[player2]}.")
        print()

    overallWinner = findWinner(wins, wins.keys())

    print(f"{overallWinner} gana el juego.")

def findWinner(wins, names):
    bestOf = 3
    for name in names:
        if wins.get(name, 0) >= bestOf:
            return name

    return None

# Ganador
def winnerCheck(player1, player2, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("¡Empate!")

    outcome = rolls.get(roll1, {})

    if roll2 in outcome.get('vence'):
        return player1
    elif roll2 in outcome.get('vencido'):
        return player2

    return winner


# Obtener Decision
def getRoll(playerName, rolls_names):
    # Inputs y Conversiones
    print("Opciones Disponibles:")
    for index, r in enumerate(rolls_names, start=1):
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
    return rolls_names[selectedIndex]  # Seleccionar de la lista


if __name__ == '__main__':
    main()

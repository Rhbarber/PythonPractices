import random


def main():
    header()
    game()


def header():
    print("---------------------------")
    print("   ¡Juego de adivinanza!")
    print("---------------------------")
    print()
    print("¡Adivina la cantidad de dulces que hay!")
    print()


def game():
    # Variables
    candyCount = random.randint(1, 100)
    attemptsLimit = 5
    attempts = 0
    while attempts < attemptsLimit:
        guess_text = input("¿Cuantos dulces crees que hay? ")
        guess = int(guess_text)
        attempts += 1
        if guess == candyCount:
            print(f"¡Ganaste! Habia {candyCount} dulces.")
            if attempts == 1:
                print(f"¡Felicidades! ¡Lo lograste en {attempts} intento!")
            else:
                print(f"¡Felicidades! ¡Lo lograste en {attempts} intentos!")
            break
        elif guess < candyCount:
            print("Muy bajo, sigue intentando.")
        else:
            print("Muy alto, sigue intentando.")

    if attempts == attemptsLimit:
        print("Ya no tienes mas intentos.")

    print("¡Adios!")


main()

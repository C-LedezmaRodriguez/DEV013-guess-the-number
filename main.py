"Importar librería random"
import random

def secret_num():
    """Genera un número random entre 1 y 100"""
    return random.randint(1,100)

def user_guess():
    """solicita al jugador que ingrese un número y revisa si es correcto"""
    while True:
        try:
            player_num = int(input("Guess the number, between 1 and 100: "))
            if 1 <= player_num <= 100:
                return player_num
            print("Please enter a number between 1 and 100")
        except ValueError:
            print("Please enter a correct number.")
def comp_guess(min_num, max_num):
    """Genera un número random entre 1 y 100 para el ordenador"""
    return random.randint(min_num, max_num)

def game_attempts(player_guess, secret_number):
    """Verifica si el intento del jugador es correcto, menor o mayor"""
    if player_guess == secret_number:
        return True, "Congratulations, you guessed the number!"
    if player_guess < secret_number:
        return False, "Your number is lower, keep trying"
    return False, "Your number is higuer, keep trying"

def game_play():
    """inicia el juego"""
    print("¡Welcome to the guess game!")

    secret_number = secret_num()
    print(secret_number)
    user_cont_attempts = 0
    comp_cont_attempts = 0
    total_user_attempts = []
    total_comp_attempts = []

    while True:
        user_cont_attempts +=1

        user_attempt = user_guess()
        total_user_attempts.append(user_attempt)
        print("User turn: ", user_attempt)
        succes,result_user = game_attempts(user_attempt, secret_number)
        print(result_user)

        if succes:
            break

        comp_cont_attempts+=1

        comp_attempt = comp_guess(1, 100)
        total_comp_attempts.append(comp_attempt)
        print("Computer turn: ", comp_attempt)
        succes,result_comp = game_attempts(comp_attempt, secret_number)
        print(result_comp)

        if succes:
            break

    print(f"The secret number was {secret_number}.")
    print(f"You made {user_cont_attempts} attempts, and those were: {total_user_attempts}")
    print(f"The computer made {comp_cont_attempts} attempts, and those were: {total_comp_attempts}")

    play_again = input("¿Do you wanna play again? (y/n): ")
    if play_again.lower() == "y":
        game_play()
    else:
        print("Thank you! See you next time")

if __name__ == "__main__":
    game_play()
    
import random

def secretNum():
    #Genera un número random entre 1 y 100
    return random.randint(1,100)


def userGuess(userInput):
    #solicita al jugador que ingrese un número y revisa si es correcto
        try:
            playerNum= int(userInput)
            return playerNum
        except ValueError:
            print("Please enter a correct number.")
def compGuess(minNum, maxNum):
    #Genera un número random entre 1 y 100 para el ordenador
    return random.randint(minNum, maxNum)

def gameAttempts(playerGuess, secretNumber):
    #Verifica si el intento del jugador es correcto, menor o mayor
    if playerGuess == secretNumber:
        return True, "Congratulations, you guessed the number!"
    elif playerGuess < secretNumber:
        return False, "Your number is lower, keep trying"
    else:
        return False, "Your number is higuer, keep trying"
    
def gamePlay():
    #inicia el juego
    print("¡Welcome to the guess game!")
    
    secretNumber = secretNum()
    print(secretNumber)
    userContAttempts = 0
    compContAttempts = 0
    totalUserAttempts = []
    totalCompAttempts = []
    
    while True:
        userContAttempts +=1
        
        userAttempt = userGuess(input("Guess the number, between 1 and 100: "))
        totalUserAttempts.append(userAttempt)
        print("User turn: ", userAttempt)
        succes,resultUser = gameAttempts(userAttempt, secretNumber)
        print(resultUser)
        
            
        if succes:
            break
        
        compContAttempts +=1
            
        compAttempt = compGuess(1, 100)
        totalCompAttempts.append(compAttempt)
        print("Computer turn: ", compAttempt)
        succes,resultComp = gameAttempts(compAttempt, secretNumber)
        print(resultComp)
        
        if succes:
            break
    
    print(f"The secret number was {secretNumber}.")
    print(f"You made {userContAttempts} attempts, and your attempts were: {totalUserAttempts}")
    print(f"The computer made {compContAttempts} attempts, and its attempts were: {totalCompAttempts}")
            
    playAgain = input("¿Do you wanna play again? (y/n): ")
    if playAgain.lower() == "y":
        gamePlay()
    else:
        print("Thank you! See you next time")
             
if __name__ == "__main__":
    gamePlay()
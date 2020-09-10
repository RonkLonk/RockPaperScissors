import random

playerScore = 0
computerScore = 0

gestureList = ["rock", "paper", "scissors"]

def generateGesture():
    return gestureList[random.randrange(0, 3)]

while True:
    playerGesture = input("Type 'Rock', 'Paper', or 'Scissors': ")

    computerGesture = generateGesture()

    print("The computer chose: " + computerGesture)

    if playerGesture == computerGesture:
        print("You draw!")

    elif playerGesture == ("rock" and computerGesture == "paper") or (playerGesture == "paper" and computerGesture == "scissors") or (playerGesture == "scissors" and computerGesture == "rock"):
        print("You lose! sorry :(")
        computerScore += 1

    else:
        print("You win! hooray!")
        playerScore += 1

    print("\nYour score:", playerScore)
    print("Computer score:", computerScore)

    input("...Press enter to play another round...")
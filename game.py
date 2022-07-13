import random
def getUserInput():
    val = input("Please choose either 'rock', 'paper', or 'scissors': ")
    return val


def validate_input(input):
   arr = ["rock", "paper", "scissors"]
   
   if input == "rock":
     print('You choose: ' + input)
   elif input =='Rock':
     print('You choose: ' + input)
   elif input =='ROCK':
     print('You choose: ' + input)
   elif input =='paper':
     print('You choose: ' + input)
   elif input == 'Paper':
     print('You choose: ' + input)
   elif input == 'PAPER':
     print('You choose: ' + input)
   elif input == 'scissors':
     print('You choose: ' + input)
   elif input == 'Scissors':
     print('You choose: ' + input)
   elif input == 'SCISSORS':
     print('You choose: ' + input)
   else:
     quit("Invalid Input!! Please try again")

def computerChoice(PlayerOne):
    arr= ["rock", "paper", "scissors"]
    computerChoice=random.choice(arr)
    print("The computer chose: " + computerChoice)

# Tie scenarios 

    if PlayerOne == "rock" and computerChoice == "rock": 
         print("It's a tie!")
    elif PlayerOne == "paper" and computerChoice == "paper":
         print("It's a tie!")
    elif PlayerOne == "scissors" and computerChoice == "scissors":
         print("It's a tie!")

# Player One wins scenarios

    elif PlayerOne == "rock" and computerChoice == "scissors":
        print("Rock crushes scissors. Player one wins!")
    elif PlayerOne == "paper" and computerChoice == "rock":
        print("Paper covers Rock. Player One wins!")
    elif PlayerOne == "scissors" and computerChoice == "paper":
        print(" Scissor cuts paper. Player One wins!")


# Computer wins scenarios

    elif PlayerOne == "rock" and computerChoice == "paper":
        print("Paper covers rock. Computer wins!")
    elif PlayerOne == "paper" and computerChoice == "scissors":
        print("Scissors cuts paper. Computer wins!")
    elif PlayerOne == "scissors" and computerChoice == "rock":
        print(" Rock crushes scissors. Computer wins!")




def main():

    print("---------------------")
    print("Welcome 'Player One'")
    print("---------------------")

    val = getUserInput()
    validate_input(val)
    computerChoice(val)
    print("---------------------")
    print("Thanks for playing. Please play again!")
    print("---------------------")


if __name__ == "__main__":
    main()
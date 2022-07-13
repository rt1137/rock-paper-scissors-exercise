
def getUserInput():
    val = raw_input("Please choose either 'rock', 'paper', or 'scissors': ")
    return val


def validate_input (input):
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

def computerChoice():
    arr= ["rock", "paper", "scissor"]


# Tie scenarios 

    if validate_input == "rock" and computerChoice == "rock": 
         print("It's a tie!")
    elif validate_input == "paper" and computerChoice == "paper":
         print("It's a tie!")
    elif validate_input == "scissors" and computerChoice == "scissors":
         print("It's a tie!")

# Player One wins scenarios

    elif validate_input == "rock" and computerChoice == "scissors":
        print("Rock crushes scissors. Player one wins!")
    elif validate_input == "paper" and computerChoice == "rock":
        print("Paper covers Rock. Player One wins!")
    elif validate_input == "scissors" and computerChoice == "paper":
        print(" Scissor cuts paper. Player One wins!")


# Computer wins scenarios

    elif validate_input == "rock" and computerChoice == "paper":
        print("Paper covers rock. Computer wins!")
    elif validate_input == "paper" and computerChoice == "scissors":
        print("Scissors cuts paper. Computer wins!")
    elif validate_input == "scissors" and computerChoice == "rock":
        print(" Rock crushes scissors. Computer wins!")




def main ():

    print("---------------------")
    print("Welcome 'Player One'")
    print("---------------------")

    val = getUserInput()
    validate_input(val)


if __name__ == "__main__":
    main()
''' 
    author: Nathaniel Vickers 
    date: 27/08/2026 
    version: 1.0 
    description: Rock Paper Scissors game 
''' 
 
# --------------------------------libraries 
import random 
 
 
# --------------------------------functions 
def options_maker(): 
    options = ["rock", "paper", "scissors"] 
 
    return options 
 
 
# --------------------------------main routine 
options = [] 
 
if (__name__ == "__main__"): 
    # make a list of options 
    options = options_maker() 
 
    # computer random choice 
    computer_choice = random.choice(options)
    
    # user choice
    user_choice = input("Rock, Paper or Scissors: ").lower()
    
    # check if user entered a valid choice
    while user_choice not in options:
        print("Please enter rock, paper or scissors")
        user_choice = input("Rock, Paper or Scissors: ").lower()
    
    # check who won
    if user_choice == computer_choice:
        print("It was {}, you chose {}, it was a draw".format(computer_choice, user_choice))
        
    elif user_choice == "rock" and computer_choice == "scissors":
        print("It was {}, you chose {}, you won".format(computer_choice, user_choice))
        
    elif user_choice == "paper" and computer_choice == "rock":
        print("It was {}, you chose {}, you won".format(computer_choice, user_choice))
        
    elif user_choice == "scissors" and computer_choice == "paper":
        print("It was {}, you chose {}, you won".format(computer_choice, user_choice))
        
    else:
        print("It was {}, you chose {}, you lost".format(computer_choice, user_choice))
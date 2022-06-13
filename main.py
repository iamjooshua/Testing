from random import choice

#A Brief Introduction
print("Welcome to the Rock-Paper-Scissors Game.\n You're going to be playing against the computer. Are you ready!!!.")

#Creating a list that stores the posssible choices
possible_choices = ["ROCK", "PAPER", "SCISSORS"]


GAME_START = True
while GAME_START:
    player_choice = input("'R' for ROCK, 'P' for PAPER or 'S' for SCISSORS: ").upper()
    for word in possible_choices:
        if word[0] == player_choice:
            player_choice = word
                    
    #Create a loop until player's choice is in possible choices
    if player_choice not in possible_choices:
        print('invalid choice')
        continue
                
    computer_choice = choice(possible_choices)
    print(f"Player => {player_choice}: CPU => {computer_choice}")

    #Comparing player's move
    if player_choice == computer_choice:
        print("It's a tie!")
        continue
    elif player_choice == "ROCK" and computer_choice == "SCISSORS":
        print("You win!🤝")
        GAME_START = False
    elif player_choice == "PAPER" and computer_choice == "ROCK":
        print("You win!🤝")
        GAME_START = False
    elif player_choice == "SCISSOR" and computer_choice == "PAPER":
        print("You win🤝!")
        GAME_START = False
    else:
        print("Computer wins!")
        GAME_START = False
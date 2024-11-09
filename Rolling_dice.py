import random

play = True
print(" Enter roll to play and stop to exit the game")
         

while play:
  
    x = random.randrange(1,10)
    y = random.randrange(1,10)
    values = (x, y)
    print("Welcome to the game rolling the dice")
        
    user_input = input('Your choice: ').lower()
    if user_input == "roll":
        play = True
        print(f"You got{values}")
        if x==y:
            print("You win!")
        else:
            print("You lose!")
    elif user_input == "stop":
     play = False
    else:
     print("Invalid input. Please enter 'roll' or 'stop'.")
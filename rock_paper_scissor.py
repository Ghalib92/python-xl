import random
choice = ("r","s","p",)
play = True

while play:
    computer_move = random.choice(choice)
    user_move = input("Select 'r' for rock, 's' for scissors and 'p' for paper and 'stop' to quit game: ").lower()
    if user_move == "stop":
       play = False   
    elif user_move !="stop" and user_move  not in  choice:
        print("Please enter a valid input!")
    elif user_move == computer_move:
        print(f"Computer chose {computer_move}. It's a tie!")
    elif (user_move == "r" and computer_move == "s") or (user_move == "s" and computer_move == "p") or (user_move == "p" and computer_move == "r"):
        print(f"Computer chose {computer_move}. You win!")
    
        
    else:
       print(f"Computer chose {computer_move}. You lose!")
    
    

 


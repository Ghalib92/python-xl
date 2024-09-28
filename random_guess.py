import random

random_no = random.rand_range(1, 10)
while True:
 try: 
    user = int(input("enter a number between 1 and 10:  "))
    if user > random_no :
        print("u loose, the number is higher")  
    elif  user < random_no : 
        print  ("u loose, the number is lower")  
    else :
        print(f"congratulations you won!The number was {random_no}")
        break
 except ValueError:
        print("Please enter a valid integer.")     

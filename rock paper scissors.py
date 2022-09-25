import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  

'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________) 

'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)

'''

print("Welcome to Rock, Paper, Scissors Game Simulator!\n")
choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: ")
print("\n")
computer_choice = random.randint(0, 2)
variants = [rock, paper, scissors]

if choice == '0':  # user chose rock - 0
    print("You chose:\n")
    print(variants[int(choice)]) 
    print("Computer chose:\n")
    print(variants[computer_choice])
    if computer_choice == 0:
        print("Draw!")
    elif computer_choice == 1:
        print("You lose!")
    else:
        print("You win!")
        
elif choice == '1':  # user chose paper -1
    print("You chose:\n")
    print(variants[int(choice)])
    print("Computer chose:\n")
    print(variants[computer_choice])
    if computer_choice == 0:
        print("You win!")
    elif computer_choice == 1:
        print("Draw!")
    else:
        print("You lose!")
        
elif choice == '2':  # user chose scissors - 2
    print("You chose:\n")
    print(variants[int(choice)])
    print("Computer chose:\n")
    print(variants[computer_choice])
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win!")
    else:
        print("Draw!")
        
else:  # if user chooses invalid number (not 0,1,2) like 3, 15 or -1
    print("No gestures were chosen.")
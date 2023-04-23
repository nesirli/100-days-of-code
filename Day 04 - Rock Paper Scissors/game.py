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

#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.

choices = [rock, paper, scissors]


while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
    user_choice = choices[user_choice]
    print("You choose: ")
    print(user_choice)

    print("Computer choose: ")
    computer_choice = random.choice(choices)
    print(computer_choice)

    if user_choice == rock:
        if computer_choice == scissors:
            print("You won!")
            break
        elif computer_choice == paper:
            print("You lose!")
            break
        else:
            print("It is a tie. Try again.")
            continue
    elif user_choice == paper:
        if computer_choice == scissors:
            print("You lose!")
            break
        elif computer_choice == rock:
            print("You win!")
            break
        else:
            print("It is a tie. Try again.")
            continue
    else:
        if computer_choice == rock:
            print("You lose!")
            break
        elif computer_choice == paper:
            print("You win!")
            break
        else:
            print("It is a tie. Try again.")
            continue
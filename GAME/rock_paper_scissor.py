import random
list=["Rock","Scissor","Paper"]

while True:
    C_count=0
    U_count=0
    user_choice=int(input('''
_________________________GAME START_________________________
IF YOW WANT TO PLAT THEN PRESS 1 OTHERVISE PRESS 2 FOR EXIT
1) Yes
2) Exit
-------------------------------------------------------------
'''))
    
    if user_choice==1:
        for a in range(1,6):
            user_input=int(input('''
Chose from these number 1,2,3
1 Rock
2 Scissor
3 Paper
\n
'''))
            if user_input==1:
                user_choice="Rock"
            elif user_input==2:
                user_choice="Scissor"
            else:
                user_choice="Paper"
            print(user_choice)
            computer_choice=random.choice(list)

            if(computer_choice==user_choice):
                print("User value= ",user_choice)
                print("Computer value= ",computer_choice)
                print("Game draw")
            elif(user_choice=="Rock" and computer_choice=="Scissor") or (user_choice=="Paper" and computer_choice=="Rock") or (user_choice=="Scissor" and computer_choice=="Paper"):
                print("User value= ",user_choice)
                print("computer value= ",computer_choice)
                print("You win>>>>>")
                U_count=U_count+1
            else:
                print("User value= ",user_choice)
                print("computer value= ",computer_choice)
                print("Computer win>>>>>")
                C_count=C_count+1

        print()

        if(U_count==C_count):
            print("Fimal game draw")
            print("User value= ",user_choice)
            print("computer value= ",computer_choice)
        elif(U_count>C_count):
            print("You win the game by ",U_count)
        else:
            print("Computer win the game by ",C_count)

    else:
        print("Thank you ~")
        break

    

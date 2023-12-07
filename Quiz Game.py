print(" Welcome To Science Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Bye")
    quit()  

name_player = input("Please enter Your Name: ")

print("Welcome :) ",name_player)

score = 0

answer = input(' What is the biggest planet in the solar system? \n ')
if answer.lower() == 'jupiter':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' What does H2O stands for? \n ')
if answer.lower() == 'hydrogen':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is the fastest animal on Earth? \n ')
if answer.lower() == 'cheetah':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('What do plants take in? \n ')
if answer.lower() == 'oxygen':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('Who invented the light bulb? \n ')
if answer.lower() == 'thomas edison':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " points")
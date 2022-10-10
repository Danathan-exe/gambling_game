### Leave this code! ###
import random
seed = input('Enter seed:')
random.seed(seed)
### Do not make changes above this line! ###
#ddebonis
#10/9/2022
# CSC1019-680-Fall22
#setting base dollar amount and setting the base gamble count
dollar = 10
count = 0
max = 0
while True:
  #random dice chance with no user input
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  #the score of both the dice added together
  score = dice1 + dice2
  #adds 1 to the count each time the loop runs.
  count +=1
#defines the max amount of money the player has aquired.  
  if dollar > max:
      max = dollar
#when you reach 0 dollars, end the program.
  if dollar <= 0:
    print("You are out of money.")
    break
#when the score equels 7 add 4.
  elif score == 7:
      dollar = dollar + 4
      print("you have " + " $" + str(dollar) + " left")
#every other score you get subtract 1.
  else:
    dollar = dollar - 1
    print("you currently have " + " $" + str(dollar) + " left")
#times that the dice were rolled.
print("you rolled the dice " + str(count -1) + " times.")
#prints out the max dollar amount the player had during the game.
print("the highest amount of money you had was $" + str(max) )

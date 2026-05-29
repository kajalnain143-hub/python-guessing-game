#secret =4
#n= int(input("Enter value of n:"))
#while True:
   #if secret==n:
      #print("you win")
     # break
   #else:
      #n= int(input("Enter value of n:"))
import random

answer = random.randint(1,50)

print("let me think of a number betwwen 1 to 50.")
Level=input("Choose the level of difficulty...Type 'easy' or 'medium'")

def guessing_game(level):
    if level=='easy':
      attempts=10

    else:
        attempts=5
    return attempts

def check_answer(guesses_No,answer,attempts):
    if guesses_No>answer:
        print("Too high Number")
        return attempts-1
    elif(guesses_No<answer):
        print("Too low Number")
        return attempts-1
    else:
        print('Congratulations,You win the game!!')
        return attempts
    
       
        
Guess_No = 0
attempts = guessing_game(Level)
while Guess_No!=answer:
   print(f"You have {attempts} remaining to guess the number.")
   Guess_No =int(input("Guess a number:"))
   attempts=check_answer(Guess_No,answer,attempts)
   if attempts==0:
       print("You lose the game")
       break
   elif(Guess_No==answer):
       break
   
   
  
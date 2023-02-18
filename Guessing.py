'''
Author - Swapnil Bondar
Description - Console Based game, with random number module use,
             Integreted the reward and entry fee to start game.
Date - 04-01-2023
'''


import random
import sys

reward = 0
Balance = 100

while True:
        print(f"--------------------------------------------------\nYour Balance is  = {Balance}")
        entry_fee = input("\n-------------------------------------------------\nDo you want to Enter [ Entry fee is Rs.10 ][yes/no] = ")
        chance = 0
        if entry_fee == "yes":
            Balance -=10
            print(f"--------------------------------------------------\nYour Balance is  = {Balance}")
            guess = random.randint(1,10)
            h = input("--------------------------------------------------\npress f to start game : ")
            while(h=="f"):
                if (chance >=3):
                    print("CRAP ...  You Ran Out Of Chances ! ! ! ")
                    break
                user_guess = int(input("Guess the Number = "))

                if user_guess == guess:
                    print("You Have Guessed Number Successfully !")
                    chance+=1
                    print(f"Number of chance = {chance}")
                    if chance == 1:
                        reward = Balance + 100
                        print(f"Reward = {reward}")
                        Balance = reward
                        break

                    elif chance == 2:
                        reward = Balance + 50
                        print(f"Reward = {reward}")
                        Balance = reward
                        break

                    elif chance >=3:
                        reward = Balance + 25
                        print(f"Reward = {reward}")
                        Balance = reward
                        break

                elif user_guess<guess:
                    print("I was Expecting a bit Higher Number ! ")
                    chance+=1

                elif user_guess > guess:
                    print("I Was Expecting a bit Lower Number !")
                    chance+=1
        else : 
            print("Thanks You for playing !")
            sys.exit()

#Generate a random number between 1 and 20 (including both). Ask the user to guess the number and let them know if their guess is too low, too high, or exactly right. 🎲
#Extras:
#Keep the game going until the user types “exit” 🔄
#Track how many guesses the user has made and show this count when the game ends 📊
#Start the user at 20 points and take one away for each guess.
#Remember the user's all time high score.
#Use Tkinter to create a GUI game interface

import random
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number = random.choice(mylist)

points = 20 
guesses_made = 0
guess = 0
print("You have 20 points, guess correctly before you run out of points. 3417 stands for exit, enter that if you want to end the game.")
while points > 0 and guess != 3417 and guess != number:
    guess = int(input("Guess a number between 1-20."))
    if guess > number:
        guesses_made += 1
        points -= 1
        print("Guess was too high.")
    elif guess < number:
        guesses_made += 1
        points -= 1
        print("Guess was too low.")
    elif guess == number:
        guesses_made += 1
        points -= 1
        print("Exactly right!")
    elif guess == 3417:
        break
    else:
        print("invalid input")

print("You had " + str(points) + " points left!")
print("You found the number after " + str(guesses_made) + " guesses!")

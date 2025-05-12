import random

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
number = random.choice(mylist)

points = 10 
guesses_made = 0
guess = 0
print("You have 10 points, guess correctly before you run out of points. 3817 stands for exit, enter that if you want to end the game.")
while points > 0 and guess != 3817 and guess != number:
    guess = int(input("Guess a number between 1-50: "))
    if guess > 50 and guess != 3817:
        print("Please guess a number within 1-50.")
        continue

    if guess == 3817:
        print("Thank you for playing! Play again")
        break
    elif guess > number:
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
        print("You had " + str(points) + " points left!")
        print("You found the number after " + str(guesses_made) + " guesses!")
    else:
        print("invalid input")

import random

myName = input("Whats your name ? ")

print("Well, " + myName + ", Im thinking of a number between 1 and 20")

secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    guess = int(input("Take a guess ? "))

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print(
        "Good job, "
        + myName
        + "! You guessed my number in "
        + str(guessTaken)
        + " guesses!"
    )
else:
    print("Nope, the number I was thinking of was " + str(secretNumber))

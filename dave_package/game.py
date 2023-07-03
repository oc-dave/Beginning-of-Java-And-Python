import random
secret_number = random.randint(1, 20)
tries = 10

print("Welcome to my Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

while tries > 0:
    print(f"You have {tries} tries left.")
    guess = int(input("Take a guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess != secret_number:
        print("wrong,try again")

        tries -= 1

if tries == 0:
    print("Sorry, you ran out of tries.")
    print(f"The secret number was {secret_number}.")

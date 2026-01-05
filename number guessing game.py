import random

secret_number = random.randint(1, 20)
attempts = 5

print("🎯 Welcome to Number Guessing Game!")
print("I have chosen a number between 1 and 20")
print("You have only 5 chances. Good luck! 😄")

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif guess > secret_number:
        print("📈 Too high!")
    else:
        print("📉 Too low!")

    attempts = attempts - 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("😢 Game Over!")
    print("The secret number was:", secret_number)

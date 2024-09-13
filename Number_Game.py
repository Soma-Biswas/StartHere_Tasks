def guess_the_number():
    target_number = 69
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if guess < target_number:
            print("Ohhh!!!!! Too low! Try again.")
        elif guess > target_number:
            print(" Keep going!! It's too high! Try again.")
        else:
            print(" Damn!!!!!Congratulations Buddy! You guessed the correct number it's:",target_number)
            break
guess_the_number()

import random
import json

def greetings():
    difficulty_array = {
        1: {"level": "Easy", "chances": 10},
        2: {"level": "Medium", "chances": 5},
        3: {"level": "Hard", "chances": 3},
    } 
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n")

    print("Please select the difficulty level:")
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n")
    difficulty = int(input("Enter your choice: "))
    print(f"\nGreat! You have selected the {difficulty_array[difficulty]['level']} difficulty level.")
    print("Let's start the game!\n")

    return [difficulty_array[difficulty]['level'], difficulty_array[difficulty]['chances']]

def comparison(guess, random_number):
    return "less" if guess < random_number else "greater" 

def game(chances, random_number):
    tries = 0 
    
    while True:
        if tries < chances:
            guess = int(input("Enter your guess: "))
            if guess != random_number:
                tries += 1
                print(f"Incorrect! The number is {comparison(random_number, guess)} than {guess}")
                if tries == chances:
                    print("You out of chances") 
                    break
            else:
                print(f"Correct! congrats. Attemps: {tries+1}")
                break
            

def main():
    while True:
        random_number = random.randint(1, 100)
        dif_level, dif_chances = greetings()
        game(dif_chances, random_number)

        against = input("Do you wanna try again this shit? (y/n) ")

        if against.lower() != "y":
            print("oka brother")
            break


if __name__ == '__main__':
    main()
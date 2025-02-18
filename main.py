from random import randint as rand
choice_list = ["Easy", "Medium", "Hard"]

def choice():
    print (f"""-- Number Guessing Game -- 
    - The goal of this game is to guess the random number correctly. 
    - Each guess will be followed with a prompt that indicates if your guess is higher or lower than the random number.
    
    Below are the difficulty levels. Select an option from the following. 
    1. {choice_list[0]}.
    2. {choice_list[1]}.
    3. {choice_list[2]}.
    """)
    try:
        choice = int(input("Enter your choice : "))
        if 1 <= choice <= 3:
            print (f"{choice_list[choice-1]} Difficulty selected.")
            return choice
        else:
            print ("Enter a valid difficulty level (1/2/3) ")

    except ValueError:
        print ("Enter a valid difficulty level (1/2/3) ")


def difficulty(choice):
    if choice == 1:
        max_range = 20
        max_attempts = 30
        target = rand(1, max_range)

    elif choice == 2:
        max_range = 100
        max_attempts = 20
        target = rand(1, max_range)

    else:
        max_range = 1000
        max_attempts = 15
        target = rand(1,1000)

    return target,max_attempts,max_range

def process(target,max_attempts,max_range):

    print (f"Hint - The generated number is between 1 and {max_range} ")
    attempts = 0

    while True:
        if attempts <= max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                if 1 <= guess <= max_range:
                    if guess > target:
                        print("Try going lower")
                        attempts += 1
                    elif guess < target:
                        print("Try going higher")
                        attempts += 1
                    else:
                        attempts += 1
                        print(f"You've got it correct! {attempts} attempts were made.")
                        break
                else:
                    print(f"Your guess should be between 1 and {max_range}")

            except ValueError:
                print(f"Invalid entry. Please provide a number between 1 and {max_range}")
        else:
            print("You've run out of attempts! Try again.")
            break

def main():
    user_choice = choice()
    pass_target,pass_attempts,pass_range = difficulty(user_choice)
    process (  pass_target,pass_attempts,pass_range)


main()
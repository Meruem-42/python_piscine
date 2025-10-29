from random import randint

def main() :
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    try_count = 0
    number_find = randint(1, 99)

    while True :
        print("What's your guess between 1 and 99?")
        number_try = input(">> ")
        if number_try == "exit" :
            return 
        try_count += 1
        try :
            if int(number_try) == number_find :
                if number_find == 42 :
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if number_try == 1 :
                    print("Congratulations, you've got it on the first try!")
                else :
                    print("Congratulations, you've got it!")
                    print(f"You won in {try_count} attempts")
                return
            elif int(number_try) > number_find :
                print("Too high!")
            if int(number_try) < number_find :
                print("Too low!")
        except ValueError :
            print("That's not a number!")

main()
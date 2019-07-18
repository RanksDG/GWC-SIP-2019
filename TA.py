
# --- Define your functions below! ---
def greetings():
    print("---------------------------")
    print("Top of the morning to Yuh")

def name(answer):
    userAnswer2 = input(f"Would you like to play a game, {answer}.Yes or no?")
    print(userAnswer2)
    return userAnswer2


def choices(response):
    if( response == 'yes'):
        print(' We are going to play Rock Paper Scissors')
    if( response == "no"):
        print('Your loss meanie')


        # --- Put your main program below! ---

def main():
    while True:
        greetings()
        # answer = input("(What will you say?) ")
        # print("That's cool!")
        a = input("What is your name ?")

        #calls the function and returns the answer
        #set response to equal our aswer which is returned from name(a)
        response1 = name(a)

        choices(response1)

        import random

        possible = [" rock, paper, scissors"]
        h = random.choice(possible)

    
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()

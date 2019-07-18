# --- Define your functions below! ---
def greetingFunction():
    print("Greetings Child")
# def introductions
#     input("whats your name")
def additionalfunction(num1,num2):
    print("I will find the sum of these two numbers")
    answer = num1 + num2
    print(f"the answer is: {answer}")

def respondToUser(userAnswer):
    if(userAnwer == "good"):
        print("I'm happy to hear, I'm good too")
    if(userAnswer == 'bad'):
        print("I'm sorry, How can I help")


# --- Put your main program below! ---
def main():
  while True:
    # answer = input("(What will you say?) ")
    # print("That's cool!")
    greetingFunction()



    user_input = input("How are you today")
    respondToUser(user_input)

    # num1 = int(input("Enter a number: "))
    # num2 = int(input("Enter your second number: "))

#     additionalFunction()
  if __name__ == "__main__":
  main()

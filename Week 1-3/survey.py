# Another way to do it
# def takesurvey(askQues,ansQues);
#     for i in range (7):
#         answer = {}
#         for q in askQues:
#             answer[q] = input(q)
#         print(answer)
#         ansQues.append(answer)
#         print(answer)

ansQues = []

askQues = ["What's the best fruit? ", "What is your name? ", "How are you today? ","Would you rather skydive or deepsea diving? "]
for i in range (2):
# or I could calm the functions
    answer = {}
    for q in askQues:
        answer[q] = input(q).lower
        #print(answer)
        ansQues.append(answer)
        #print(answer)
    print("THANK YOU FOR TAKING MY SURVEY :)")



# print(input(What is better? Apple or Banana))
#if answer = apple ask what is better apple juice or milk
#if answer = banana ask what is better banana juice or milk
#if answer = milk say yucky
#if answer = apple juice say an apple a day keeps the doctor away
#if answer = banana juice say oooh watch yourself
# at the end print thank you for taking our survey

def greetings():
    print("hello world")
greetings()
display = ""
print ("ok?")
i = 0
while True:
    i += 1
    if i > 10:
        display += "?"
    else:
        display += "@"
    print(display)

userInput = int(input("Enter user input"))
while(userInput<20):
    print("First Input"+str(userInput))
    if(userInput==13 or userInput==14):
        userInput = userInput+1
        continue
    else:
        print(userInput)
        userInput = userInput+1

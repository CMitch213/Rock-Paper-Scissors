import random

selection = ""
ai = 0
tie = "It's a tie!"
win = "You WIN!!!"
loss = "You LOSE!!!"
aiWords = ""
print("---   Welcome to ROck Paper Scisoors!!!   ---")
print("Input 1 for Rock, 2 for Paper, 3 for Scissors")
inp = input("Enter answer here:")

if inp == "1":
    selection = "Rock"
elif inp == "2":
    selection = "Paper"
elif inp == "3":
    selection = "Scissors"
else:
    print("Error: Invalid Selection")

ai = random.randint(1,3)
if ai == 1:
    aiWords = "Rock"
elif ai == 2:
    aiWords = "Paper"
else:
    aiWords = "Scissors"

print("ai played:", aiWords)

if selection == aiWords:
    print(tie)
elif selection == "Rock" and aiWords == "Paper":
    print(loss)
elif selection == "Rock" and aiWords == "Scissors":
    print(win)
elif selection == "Paper" and aiWords == "Rock":
    print(win)
elif selection == "Paper" and aiWords == "Scissors":
    print(loss)
elif selection == "Scissors" and aiWords == "Rock":
    print(loss)
elif selection == "Scissors" and aiWords == "Paper":
    print(win)

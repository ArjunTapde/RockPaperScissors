import random
import time

optionList = ["Rock", "Paper", "Scissors"]
print("Let's play a game of Rock Paper Scissors!!")
time.sleep(.5)
consent = input("Please enter: Y/N\n")

if (consent == "N"):
    print("Oh sad! Maybe another time!!")
    exit()
elif (consent == "Y"):
    print("Great! Let us begin!!")


time.sleep(.5)
print("Rock!")
time.sleep(.5)
print("Paper!")
time.sleep(.5)
print("Scissors!")
time.sleep(.5)

humanValue = input("Your move: ")
time.sleep(.75)

print("SHOOT!!")
cpuValue = random.choice(optionList)
time.sleep(1)

if (humanValue != cpuValue):
    if (cpuValue == "Rock"):
        if (humanValue == "Paper"):
            print("YOU WON!!")
        if (humanValue == "Scissors"):
            print("Oh no, you lost!!")
    if (cpuValue == "Paper"):
        if
    if (cpuValue == "Scissors"):
        if
elif (humanValue == cpuValue):
    print("DRAW!!")
    #add replay function and play again option



import random
import time

playing = True
optionList = ["Rock", "Paper", "Scissors"]
print("Let's play a game of Rock Paper Scissors??")
time.sleep(.5)
consent = input("Please enter: Y/N\n")

if (consent == "N"):
    print("Oh sad! Maybe another time!!")
    exit()
elif (consent == "Y"):
    print("Great! Let us begin!!")

while playing == True:
    time.sleep(.5)
    print("Rock!")
    time.sleep(.5)
    print("Paper!")
    time.sleep(.5)
    print("Scissors!\n")
    time.sleep(.5)

    humanValue = input("Your move: ")
    time.sleep(.75)

    print("SHOOT!!\n")
    cpuValue = random.choice(optionList)
    time.sleep(1.5)

    if (humanValue != cpuValue):
        if (cpuValue == "Rock"):
            if (humanValue == "Paper"):
                print("YOU WON!!")
            if (humanValue == "Scissors"):
                print("Oh no, you lost!!")
        if (cpuValue == "Paper"):
            if (humanValue == "Scissors"):
                print("YOU WON!!")
            if (humanValue == "Rock"):
                print("Oh no, you lost!!")
        if (cpuValue == "Scissors"):
            if (humanValue == "Rock"):
                print("YOU WON!!")
            if (humanValue == "Paper"):
                print("Oh no, you lost!!")
    elif (humanValue == cpuValue):
        print("DRAW!!")

    time.sleep(1)
    print("I chose: " + cpuValue + "\n")

    time.sleep(1)
    print("Would you like to play again?")
    reConsent = input("Please enter: Y/N\n")

    if (reConsent == "N"):
        print("It was great playing with you, goodbye!!")
        exit()
    elif (reConsent == "Y"):
        print("Great! Let's play again!!")




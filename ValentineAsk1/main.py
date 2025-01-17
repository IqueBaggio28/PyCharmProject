import time

loop_ask = True

while loop_ask:
    name = input("Please type your full name: ")
    age = int(input("Please type your age: "))
    dog_name = input("Please type the name of your dog: ")

    print ("Checking data")
    for i in range(3):
        print(".")
        time.sleep(1)

    if name == "Dominique Isabella Loyd" or name == "dominique isabella loyd" and age == 20 and dog_name == "Zelda" \
            or dog_name == "zelda":
        print("Access granted.")
        loop = True
        loop_ask = False

    else:
        print("Access denied, try again.")
        time.sleep(1)

while loop:


    response = input("Hey Mimi, do you want to be my valentine :) ? \n\n\t(Y) - Yes\n\t(N) - No \n")
    if response == 'y' or response == 'Y':
        loop2 = True
        loop = False
        while loop2:
            response2 = input("Are you sure???\n\t(Y) - Yes\n\t(N) - No \n")

            if response2 == 'y' or response2 == 'Y':
                loop2 = False

            else:
                continue

    else:
        continue
time.sleep(0.5)
print("YEEPPYYYYYY!!\nLove you babe! <3")

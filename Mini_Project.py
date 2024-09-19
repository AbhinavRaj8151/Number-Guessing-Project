import random




target = random.randint(1,100)


while True:

    userChoice = int(input("Enter a number between 1 to 100 to guess the target:"))

    if(userChoice > target):

        print("ooh Noo, your choice is greater than the target try again!!")

    elif(userChoice < target):

        print("Ooh Noo, your choice is smaller than the target try again!!")

    else:

        print("Congratulation!! your choice is same as target:","userChoice",userChoice, "=","target", target)
        print("-----GAME OVER !!!-----")
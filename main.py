def game():
    print('You are outside the McDonalds.')
    move = input("What do you want to do?: ")

#Game
    if move == "forward":
        print("You are inside the McDonalds.")
        move = input("What do you want to do?: ")
        forward(move)


    elif move == "left":
        print("You are at the left corner of the building")
        move = input("What do you want to do?: ")
        outside_right(move)

    elif move == "right":
        print("You are bottom right corner.")
        move = input("What do you want to do?: ")
        outside_left(move)

#Game Function
def forward(move):
    if move == "left":
        print("Ronald is close by.")
        move = input("What do you want to do?: ")
    else:
        print("You cant go there.")
        if move == "right":
            print("You died.")
            replay()
        else:
            print("You cant go there.")
    if move == "forward":
        print("Youre in the middle of the store.")
        move = input("What do you want to do?: ")
    else:
        print("You cant go there.")
        if move == "right":
            print("You are infront of the register.")
            move = input("What do you want to do?: ")
        else:
            print("You cant go there.")
            if move == "buy":
                print("You bought a Hamburger")
                move = input("What do you want to do?: ")
                after_buy(move)
            else:
                print("You cant go there.")

def outside_right(move):
    if move == "right":
        print("You are at the left corner of the building")
        move = input("What do you want to do?: ")
        if move == "right":
            print("Youre in front of the back door")
            move = input("What do you want to do?: ")
            if move == "forward":
                print("Youre at the top right corner of the building")
                move = input("What do you want to do?: ")
                if move == "right":
                    print("Youre infront of the dumpster")
                    move = input("What do you want to do?: ")
                    if move == "forward":
                        print("Youre at the bottom bottom right corner.")
                        move = input("What do you want to do?: ")
                        if move == "right":
                            print("You are infront of the Mcdonalds")
                            move = input("What do you want to do?: ")

def outside_left(move):
    if move == "left":
        print("Youre infront of the dumpster")
        move = input("What do you want to do?: ")
        if move == "forward":
            print("Youre at the top right corner of the building")
            move = input("What do you want to do?: ")
            if move == "left":
                print("Youre in front of the back door")
                move = input("What do you want to do?: ")
                if move == "forward":
                    print("You are at the left corner of the building")
                    move = input("What do you want to do?: ")
                    if move == "forward":
                        print("You are at the top left corner of the building")
                        move = input("What do you want to do?: ")
                        if move == "left":
                            print("You are at the bottom left corner of the building")
                            move = input("What do you want to do?: ")
                            if move == "left":
                                print("You are infront of the Mcdonalds")
                                move = input("What do you want to do?: ")

def after_buy(move):
    items = ["Hamburger", "Soda"]

    if move == "back":
        print("")

    else:
        print("You cant go there.")

    if move == "":
        print("you have given the man the burger and a soda")
        print("He has helped you escape the Mc.Donalds, congratulations")
        break
    else:
        print("you must have the burger and soda to talk to the man")
def replay():
    replay = input("Would you like to play again?: ")

    if replay == "Yes":
        game()
    else:
        print("Closing...")

game()
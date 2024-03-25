import random

player = 0
computer = 0
num_to_str = ""
num_to_str_for_computer = ""
answer = ""
running = True

def reset():
    global player
    global computer
    global num_to_str
    global num_to_str_for_computer
    global answer
    global running
    player = 0
    computer = 0
    num_to_str = ""
    num_to_str_for_computer = ""
    answer = ""
    running = True

while running:
    player = int(input("가위:1  바위:2  보:3\n\n"))
    print("\n")

    if player < 1 or player > 3:
        print("error\n\n")

    computer = random.randrange(1, 4)

    if player == 1:
        num_to_str = "가위"

    elif player == 2:
        num_to_str = "바위"

    elif player == 3:
        num_to_str = "보"

    if computer == 1:
        num_to_str_for_computer = "가위"

    elif computer == 2:
        num_to_str_for_computer = "바위"

    elif computer == 3:
        num_to_str_for_computer = "보"

    if player == computer:
        print("나: %s" % num_to_str)
        print("상대방: %s" % num_to_str_for_computer)
        print("비김\n\n")



    if player == 1:
        if computer == 2:
            print("나: %s" % num_to_str)
            print("상대방: %s" % num_to_str_for_computer)
            print("짐\n\n")

        else:
            print("나: %s" % num_to_str)
            print("상대방: %s" % num_to_str_for_computer)
            print("이김\n\n")


    if player == 2:
        if computer == 3:
            print("나: %s" % num_to_str)
            print("상대방: %s" % num_to_str_for_computer)
            print("짐\n\n")

        else:
            print("나: %s" % num_to_str)
            print("상대방: %s" % num_to_str_for_computer)
            print("이김\n\n")



    if player == 3:
        if computer == 1:
            print("나: %s" % num_to_str)
            print("상대방: %s" % num_to_str_for_computer)
            print("짐\n\n")

        else:
            print("나: %s" % num_to_str)
            print("상대방: %s" % num_to_str_for_computer)
            print("이김\n\n")

    answer = input("again:a or quit for any key except a\n\n")

    if answer == "a":
        reset()
        print("\n\n")

    else:
        running = False


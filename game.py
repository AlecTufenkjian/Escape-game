from sys import argv
script, image, image_2 = argv


def start():
    print("Please enter your name:")
    name = input(">>> ")
    print(f"""
    Hello {name}, welcome to the escape house!
    In this game, your goal is to get out of this house as soon as possible!
    The door from which you have to get out is locked with an 8 digit combination lock.

    To begin with, you have to walk around picking up items you find on your way.
    It is your job to find out how and where to use the items in order to escape.
    To pick up something, type for example "pick up x"
    To use things, type for exmple "combine x and y"
    """)

def start_2():
    print("Are you ready?")
    ready = input(">>> ")
    if "yes" in ready:
        start_3()
    elif "no" in ready:
        print("Man, it's not even a question")
        txt = open(image, encoding="utf8")
        print(txt.read())
        start_3()
    else:
        print("Man, learn how to type yes or no")
        txt = open(image, encoding="utf8")
        print(txt.read())
        start_2()


def start_3():
    print("""
    Okay let's start. The house you're trapped in is composed of 6 rooms, one of which is the center and the other 5 around.
    You're right now in the middle room which will be also referred to room 6. Feel free to enter any room by typing for example \"enter room 1\"
    Now, try going around.
    """)

    door_opened = False
    room_1 = False
    room_2 = False
    room_3 = False
    room_4 = False
    room_5 = False
    room_6 = True

    list = [room_1, room_2, room_3, room_4, room_5, room_6]
    items = []
    items_game = ["key", "drawer", "screwdriver", "pencil sharpner", "locked box", "door"]

    while door_opened == False:
        room = input(">>> ")
        if "enter room" in room:
            if int(room[11:]) in range(1,7):
                x = list.index(True)
                list[x] = False
                a = int(room[11:]) - 1
                list[a] = not(list[a])
                print("access for room", room[11:], "is granted")
                print(list)
                print("In this room, there is:", items_game[a])
            else:
                print("Learn how to type idiot")
        elif "pick up" in room:
            if room[8:] in items_game:
                abc = room[8:]
                pick_up(abc, list, items, items_game)
                print("You have now:", items)
            else:
                print("Learn how to type idiot")
        elif "combine" in room:
            if room == "combine key and drawer" or room == "combine drawer and key":
                if "key" in items and "drawer" in items:
                    items.append("plastic binder")
                    items.remove("key")
                    items.remove("drawer")
                    print("You have now:", items)

            elif room == "combine screwdriver and pencil sharpner" or room == "combine pencil sharpner and screwdriver":
                if "screwdriver" in items and "pencil sharpner" in items:
                    items.append("sharp piece of metal")
                    items.remove("screwdriver")
                    items.remove("pencil sharpner")
                    print("You have now:", items)

            elif room == "combine plastic binder and sharp piece of metal" or room == "combine sharp piece of metal and plastic binder":
                if "plastic binder" in items and "sharp piece of metal" in items:
                    items.append("master key")
                    items.remove("plastic binder")
                    items.remove("sharp piece of metal")
                    print("You have now:", items)

            elif room == "combine master key and locked box" or room == "combine locked box and master key":
                if "master key" in items and "locked box" in items:
                    items.remove("master key")
                    items.remove("locked box")
                    print("The password is SURPRISE MOTHAFACKA, go to room 6 and enter 'door.SURPRISE MOTHAFACKA' for a surprise")

            else:
                print("There is no such combination, idiot")

        elif "door.SURPRISE MOTHAFACKA" in room:
            if room_6 == True:
                txt_2 = open(image_2, encoding="utf8")
                print(txt_2.read())
                door_opened = True
            else:
                print("Learn how to type idiot")
        else:
            print("Learn how to type idiot")


def pick_up(item, list, items, items_game):
    zz = items_game.index(item)
    if list[zz] == True:
        items.append(item)

start()
start_2()

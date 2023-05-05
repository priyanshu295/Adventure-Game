import time

def intro():
    print("Welcome to 360 Adventure Game!")
    time.sleep(2)
    print("You wake up in a dark room with no memory of how you got there.")
    time.sleep(2)
    print("You see a door in front of you.")
    time.sleep(2)

def door():
    print("You approach the door and try the handle.")
    time.sleep(2)
    print("It's locked.")
    time.sleep(2)
    print("You notice a keyhole.")
    time.sleep(2)
    print("You can either:")
    print("a. Look for the key.")
    print("b. Try to break down the door.")

    choice = input("Enter your choice (a/b): ")

    if choice == "a":
        print("You look around the room and find a key hidden under the bed.")
        time.sleep(2)
        print("You use the key to unlock the door.")
        time.sleep(2)
        print("You step through the door into a long hallway.")
        hallway()
    elif choice == "b":
        print("You try to break down the door, but it's too sturdy.")
        time.sleep(2)
        print("You need to find another way out.")
        time.sleep(2)
        door()
    else:
        print("Invalid choice.")
        time.sleep(2)
        door()

def hallway():
    print("You walk down the hallway and come to a fork in the path.")
    time.sleep(2)
    print("You can either:")
    print("a. Go left.")
    print("b. Go right.")

    choice = input("Enter your choice (a/b): ")

    if choice == "a":
        print("You turn left and come to a door.")
        time.sleep(2)
        print("You can either:")
        print("a. Try the door.")
        print("b. Go back.")

        choice = input("Enter your choice (a/b): ")

        if choice == "a":
            print("You try the door, but it's locked.")
            time.sleep(2)
            print("You need to find the key.")
            time.sleep(2)
            hallway()
        elif choice == "b":
            print("You turn back and come to the fork in the path.")
            time.sleep(2)
            hallway()
        else:
            print("Invalid choice.")
            time.sleep(2)
            hallway()

    elif choice == "b":
        print("You turn right and come to a staircase.")
        time.sleep(2)
        print("You can either:")
        print("a. Go up the staircase.")
        print("b. Go back.")

        choice = input("Enter your choice (a/b): ")

        if choice == "a":
            print("You climb the staircase and come to a door.")
            time.sleep(2)
            print("You try the handle and it opens.")
            time.sleep(2)
            print("You step through the door into the sunlight.")
            time.sleep(2)
            print("Congratulations! You've escaped the adventure game!")
        elif choice == "b":
            print("You turn back and come to the fork in the path.")
            time.sleep(2)
            hallway()
        else:
            print("Invalid choice.")
            time.sleep(2)
            hallway()

intro()
door()

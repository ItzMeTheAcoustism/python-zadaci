nicknames = []
max_capacity = 5

while True:
    choice = input("Enter, leave, read room status or exit program? ")
    if choice == 'enter':
        if len(nicknames) < max_capacity:
            nickname = input("Enter your nickname: ")
            nicknames.append(nickname)
            print(f"{nickname} has entered the room.")
        else:
            print("There isnt room. Wait. ")
    elif choice == 'leave':  
        nickname = input("Enter your nickname: ")
        if nickname in nicknames:
            nicknames.remove(nickname)
            print(f"{nickname} has left the room.")
        else:
            print(f"{nickname} is not in the room.")
    elif choice == 'read room state' or choice == "read":  
        if nicknames:
            print("People currently in the room: " + ", ".join(nicknames))
        else:
            print("The room is currently empty.")
    elif choice == "exit" or  choice == "exit program":
        print("Exiting program.")
        break
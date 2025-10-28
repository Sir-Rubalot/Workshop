community = []

def add_user(community):
    add_user = input("New username: ")
    if add_user == "":
        print("Please enter a valid username")
    else:
        community.append(add_user)
        print("User created!")

def log_in(community):
    log_in = input("Enter username: ")
    if log_in == add_user:
        print("Enter your password: ")

def remove_user(community):
    if len(community) == 0:
        print("playlist is empty")
        return
    
    show_members(community)
    
    print("---DevOps community---")
    for i, song in enumerate(community, start=1):
        print(f"{i}: {song}")

    user_to_remove = (input("Which user do you want to remove?: ")).strip()
    if not user_to_remove.isdigit():
        print("Not a number!!!")

    user_number = int(user_to_remove)
    if user_number < 1 or user_number >len(community):
        print("Not in range of playlist, idiot")

    remove_song = community.pop(user_number - 1)
    print (f"success! Removed user {remove_user}")

def show_members(community):
    if len(community) == 0:
        print("Community is empty")

    print("---DevOps Community---")
    for i, song in enumerate(community, start=1):
        print(f"{i}: {song}")

def main():
    while True:
        print("===DevOps community===")
        print("1) Register new user")
        print("2) Log in")
        print("3) Remove user")
        print("4) Show members")
        print("0) Exit menu")
        user_choice = input(">: ").strip()

        if user_choice == "1":
            add_user(community)
        elif user_choice == "2":
            log_in(community)
        elif user_choice == "3":
            remove_user(community)
        elif user_choice == "4":
            show_members(community)
        elif user_choice == "0":
            break
        else:
            print("Invalid choice")

main()
community = []

def add_user():
    username = input("New username: ").strip()
    password = input("New password: ").strip()
    if add_user == "":
        print("Please enter a valid username")
        return
    elif any(user['username'] == username for user in community):
        print("Username already taken, dummy!")
        return
    
    community.append({'username': username, 'password': password})
    print("User created!")

def log_in():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    for user in community:
        if user['username'] == username and user['password'] == password:
            print("Log in successful!")
            return
        print("username or password incorrect")

def remove_user():
    if not community:
        print("Community is empty")
        return
    
    show_members()
    
    user_to_remove = input("Which user do you want to remove?: ").strip()
    for i, user, in enumerate(community):
        if user ['username'] == user_to_remove:
            community.pop(i)
            print(f"Successfully removed {user_to_remove}")
            return

def show_members():
    if not community:
        print("Community is empty")
        return

    print("---DevOps Community---")
    for i, user in enumerate(community, start=1):
        print(f"{i}: {user['username']}")

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
            add_user()
        elif user_choice == "2":
            log_in()
        elif user_choice == "3":
            remove_user()
        elif user_choice == "4":
            show_members()
        elif user_choice == "0":
            break
        else:
            print("Invalid choice")
main()

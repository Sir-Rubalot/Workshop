news_galaxy = []

adresser = set()
#while True:
#    epost = input("Ange e-postadress för att signa upp till nyhetsbrevet! ").strip()
#    user_choice = input(">: ").strip()
#    if epost.lower() == 'sluta':
#        break
#    adresser.add(epost)

total = len(adresser)
unika = len(news_galaxy)

def add_email(adresser):
    user_email = input("New email: ")
    if user_email == "":
        print("Please enter a valid email")
    else:
        adresser.append(user_email)
        print("User added!")

def show_List(adresser):
    if len(adresser) == 0:
        print("News Galaxy is empty")
        return
    print("---Newsletter for the Galaxy---")
    for i, epost in enumerate(adresser, start=1):
        print(f"{i}: {epost}")

def remove_duplicates(adresser):
    unika = []
    for epost in adresser:
        if epost not in unika:
            unika.append(epost)
        return unika

def main():
    while True:
        print("=== Galaxy Newsletter ===")
        print("1> Add new email")
        print("2> Show list of email")
        print("3> Remove duplicates")
        print("0> Exit menu")
        user_choice = input(">: ").strip()

        if user_choice == "1":
            add_email(news_galaxy)
        elif user_choice == "2":
            show_List(news_galaxy)
        elif user_choice == "3":
            remove_duplicates(news_galaxy)
        elif user_choice == "0":
            break
        else:
            print("Invalid choice")
        
        domäner = {}
        for e in news_galaxy:
            if "@" in e:
                domän = e.split("@")[-1]
                domäner[domän] = domäner.get(domän, 0) + 1
        
        print(f"Totalt antal adresser: {len(news_galaxy)}")
        print(f"Unika adresser: {len(set(news_galaxy))}")
        print("Domänöversikt: ")
        for domän, antal in domäner.items():
            print(f"{domän}: {antal}")

main()
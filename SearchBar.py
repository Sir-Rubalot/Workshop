search_bar = []

word_bank = ["apple", "samsung", "banana", "application", "python", "apartment", "skateboard", "bycycle", "robots"]

def autofill(prefix, word_bank, max_match=5):
    matching = []
    for word in word_bank:
        if word.startswith(prefix):
            matching.append(word)

    matching.sort()
    return matching[:max_match]

while True:
    prefix = input("Skriv ett prefix (eller 'q' för att avsluta): ")
    if prefix.lower() == 'q':
        break
    matches = autofill(prefix, word_bank)
    print("Menade du:")
    for match in matches:
        print(match)
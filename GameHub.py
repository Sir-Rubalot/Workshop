import heapq

K = 3
top_scores = []

def add_score(score):
    if len(top_scores) < K:
        heapq.heappush(top_scores, score)
    else:
        if score > top_scores[0]:
            heapq.heapreplace(top_scores, score)

def get_top_k():
    return sorted(top_scores, reverse=True)

print("Välkommen till Arkadhallen!!")

while True:
    user_input = input("Vad är din poäng: ")
    if user_input.lower() == 'stop':
        break
    try:
        poäng = int(user_input)
        add_score(poäng)
        print("The highest scores right now is: ", get_top_k())
    except ValueError:
        print("Sluta fuska, skriv poäng i siffror!!")

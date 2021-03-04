import random
from os import system, name

def Clear():
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

def Continue():
    input("Press Enter to continue...")

def SetPlayers():
    while True:
        try:
            num_of_players = int(input("How many players?: "))
        except ValueError:
            print("Not a valid input")
        else:
            if num_of_players > 1:
                break
            else:
                print("Impossible amount!")
    players = []
    for x in range(1, num_of_players+1):
        players.append(input(f"player {x} name: "))
    return players

def SetOrder(players):
    random.shuffle(players)
    return players

def SetScore(order):
    scores = {}
    for i in order:
        scores.update({i : []})
    return scores

def Judge(i):
    if i == 1:
        ordinal = "st"
    elif i == 2:
        ordinal = "nd"
    elif i == 3:
        ordinal = "rd"
    else:
        ordinal = "th"
    while True:
        try:
            score = float(input(f"{i}{ordinal} judge score: "))
        except ValueError:
            print("Not a number!")
        else:
            if 0 <= score <= 10:
                break
            else:
                print("Not a valid score!")

    return score

def TotalScores(scores):
    for player in scores:
        player_scores = sorted(scores[player], reverse=True)[:5]
        player_total = sum(player_scores)
        scores.update({player:player_total})
    return scores
    
Clear()
print(''' 
███████ ████████ ██████  ███████ ███████ ████████ 
██         ██    ██   ██ ██      ██         ██    
███████    ██    ██████  █████   █████      ██    
     ██    ██    ██   ██ ██      ██         ██    
███████    ██    ██   ██ ███████ ███████    ██    
                                                  
                                                  
██      ███████  █████   ██████  ██    ██ ███████ 
██      ██      ██   ██ ██       ██    ██ ██      
██      █████   ███████ ██   ███ ██    ██ █████   
██      ██      ██   ██ ██    ██ ██    ██ ██      
███████ ███████ ██   ██  ██████   ██████  ███████                                                
''')
input("Press ENTER to start!")
Clear()
players = SetPlayers()
order = SetOrder(players)

Clear()
print("The order is:\n")
position = 1
for i in order:
    print(position, i)
    position += 1
print("\n")
Continue()
Clear()

scores = SetScore(order)
score = 0
run_count = 0

for run in range(7):
    run_count += 1
    for x in order:
        print(f"{x}'s run {run_count}")
        for i in range(1, len(players)):
            score += Judge(i)
        final_score = round(score / (len(players)-1), 2)
        print(f"\n{x}'s run {run_count} final score: {final_score}\n")
        scores[x].append(final_score)
        score = 0
        Continue()
        Clear()

final_scores = TotalScores(scores)
dict(sorted(final_scores.items(), key=lambda item: item[1]))

print("FINAL RESULTS:")
for x, y in final_scores.items():
    print(x, y)
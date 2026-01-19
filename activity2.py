winning = {10,11,8,1,5,20}
players = {
    "Jo":{1,8,10,27,12,15},
    "JoJo":{1,8,27,3,4,9},
    "Joe":{9,4,3,12,15,21},
    }


for player, num in players.items():
    result = num & winning

    if len(result) > 0:
        total = len(result)*100
        print(f"{player} won {total} pesos!")
    else:
        print(f"{player} won nothing!")

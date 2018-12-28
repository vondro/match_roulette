import random
import itertools
import json

fl = open('list.txt', 'r')

players = []
for line in fl:
    players.append(line.rstrip())

fl.close()

# number of players
no_play = len(players)

# we want to generate list of unique tupples

random.shuffle(players)

pairs = list(itertools.combinations(players, 2))

random.shuffle(pairs)

# distribute games fairly - no one plays twice
fair_dist = []
last_players = []
processed = []
while len(pairs) > 0:
    for i in range(len(pairs)):
        if (pairs[i][0] not in last_players and pairs[i][1] not in last_players) or len(pairs) < 5:
            fair_dist.append(pairs[i])
            last_players = list(pairs[i])
            del pairs[i]
            break

out = open('pairs.txt', 'w')
out_json = open('pairs.json', 'w')
dict_json = {}
i = 1
for line in fair_dist:
    pair = str(i) + ': ' + line[0] + ' vs. ' + line[1] + '\n'
    out.writelines(pair)

    dict_json[i] = line[0] + ' vs. ' + line[1]

    i += 1

out_json.writelines(json.dumps(dict_json))
    
out.close()
out_json.close()
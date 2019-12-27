import random
import itertools
import json

fl = open('list.txt', 'r', encoding='utf-8')

players = []
for line in fl:
    players.append(line.rstrip())


#print(players)

fl.close()

# number of players
no_play = len(players)

# number of groups
no_group = 2

# we want to generate one or more lists of unique tupples

random.shuffle(players)

groups=[players[x:x+(no_play//no_group)] for x in range(0, no_play, (no_play//no_group))]

#print(groups)

# if the last group is with 1 player -> join it with the second-to-last group
if len(groups[-1]) == 1:
    groups[-2]=groups[-2]+groups[-1]
    del(groups[-1])

pairs = []

for players in groups:
    print(players)
    pairs += list(itertools.combinations(players, 2))

#print(pairs)

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

out = open('pairs.txt', 'w', encoding='utf-8')
out_json = open('pairs.json', 'w', encoding='utf-8')
out_groups = open('groups.txt', 'w', encoding='utf-8')
dict_json = {}

# write pairs to txt and json
i = 1
for line in fair_dist:
    pair = str(i) + ': ' + line[0] + ' vs. ' + line[1] + '\n'
    out.writelines(pair)

    dict_json[i] = line[0] + ' vs. ' + line[1]

    i += 1

out_json.writelines(json.dumps(dict_json))
    
out.close()
out_json.close()

# write groups to txt
i=1
for group in groups:
    out_groups.write("\nSkupina " + str(i) + ":\n")
    for line in group:
        out_groups.writelines(line + '\n')

    i+=1

out_groups.close()
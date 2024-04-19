import random
from itertools import combinations


# Global variable
NO_GROUP = 2  # Example value, set this to the number of desired groups

def generate_round_robin_pairs(players):
    if len(players) % 2:
        players.append(None)  # Add a dummy player for bye if player count is odd
    n = len(players)
    schedule = []
    for round in range(n - 1):
        round_pairs = []
        for i in range(n // 2):
            if players[i] is not None and players[n - 1 - i] is not None:
                round_pairs.append((players[i], players[n - 1 - i]))
        schedule = schedule + round_pairs
        # Rotate players for next round, keeping first player fixed
        players = [players[0]] + players[-1:] + players[1:-1]
    return schedule


def interleave_group_schedules(groups):
    schedules = [generate_round_robin_pairs(group) for group in groups]
    max_schedule_length = max(len(schedule) for schedule in schedules)
    final_schedule = []

    for round_number in range(max_schedule_length):
        for schedule in schedules:
            if round_number < len(schedule):
                final_schedule.append(schedule[round_number])

    return final_schedule


# Read the players from a file
with open('list.txt', 'r') as file:
    players = [line.strip() for line in file.readlines()]

# Shuffle the players and divide them into groups as evenly as possible
random.shuffle(players)
group_size = len(players) // NO_GROUP
groups = [players[i:i + group_size] for i in range(0, len(players), group_size)]

# If the last group has fewer players, distribute them among other groups
while len(groups[-1]) < group_size:
    for i in range(len(groups)-1):
        if len(groups[-1]) == 0:
            groups.remove(groups[-1])
            break
        groups[i].append(groups[-1].pop())

# Generating round-robin pairings for each group
final_schedule = interleave_group_schedules(groups)

position = 1

# Print out the final schedule
for match in final_schedule:
    print(f"{position}: {match[0]} vs. {match[1]}")
    position += 1
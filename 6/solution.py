import numpy as np

data = [int(x) for x in open('input.txt').read().strip().split(',') if x]
fish = np.array(data)

# Part 1
DAYS = 80

def tick(fish):
    return fish - 1

def check(fish):
    num_new_fish = np.sum(fish < 0)
    new_fish = np.full(num_new_fish, 8)

    fish = np.where(fish < 0, 6, fish)
    fish = np.append(fish, new_fish)
    return fish


for day in range(DAYS):
    fish = tick(fish)
    fish = check(fish)

print(len(fish))

# Part 2
import collections
DAYS = 256

fishc = collections.Counter(data)

def tick2(fishc):
    return {c - 1: v for c, v in fishc.items()}

def check2(fishc):
    if -1 in fishc:
        fishc[8] = fishc[-1]
        fishc[6] = fishc[-1] + fishc[6] if 6 in fishc else fishc[-1]
        fishc.pop(-1)
    return fishc

for day in range(DAYS):
    fishc = tick2(fishc)
    fishc = check2(fishc)

print(sum(fishc.values()))

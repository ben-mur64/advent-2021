import statistics
import math

data = [int(x) for x in open('input.txt').read().strip().split(',') if x]

# Part 1
med = statistics.median(data)
dists = [abs(x - med) for x in data]

print(med)
print(sum(dists))

# Part 2
def distance(val, point):
    n = abs(val - point)
    return (n ** 2 + n) / 2

## This is a very ugly brute force method, but hey, it works
def alignment(data):
    med = 0
    dist = math.inf
    for i in range(min(data), max(data)):
        dists = [distance(x, i) for x in data]
        if sum(dists) < dist:
            dist = sum(dists)
            med = i

    return med, dist

med, dist = alignment(data)

print(med)
print(dist)

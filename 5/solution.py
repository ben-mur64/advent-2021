data = [x.rstrip() for x in open('input.txt').readlines() if x]

# Gets the corrected range between two coordinates
def get_range(a, b):
    if a < b:
        return range(a, b + 1)
    if a > b:
        return range(a, b - 1, -1)
    if a == b:
        return []


# Part 1
matrix = [[0 for y in range(1000)] for x in range(1000)]
for row in data:
    vals = [[int(y) for y in x.strip().split(',')] for x in row.split('->')]
    x1 = vals[0][0] 
    x2 = vals[1][0]
    xran = get_range(x1, x2)

    y1 = vals[0][1]
    y2 = vals[1][1]
    yran = get_range(y1, y2)

    if x1 == x2:
        for y in yran:
            matrix[y][x1] += 1
    elif y1 == y2:
        for x in xran:
            matrix[y1][x] += 1

total = sum(sum(1 for x in row if x > 1) for row in matrix)
print(total)

# Part 2
matrix = [[0 for y in range(1000)] for x in range(1000)]
for row in data:
    vals = [[int(y) for y in x.strip().split(',')] for x in row.split('->')]

    x1 = vals[0][0] 
    x2 = vals[1][0]
    xran = get_range(x1, x2)

    y1 = vals[0][1]
    y2 = vals[1][1]
    yran = get_range(y1, y2)

    if xran and yran:
        for x, y in zip(xran, yran):
            matrix[y][x] += 1
    elif x1 == x2:
        for y in yran:
            matrix[y][x1] += 1
    elif y1 == y2:
        for x in xran:
            matrix[y1][x] += 1

total = sum(sum(1 for x in row if x > 1) for row in matrix)
print(total)

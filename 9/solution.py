data = [[int(y) for y in x.strip()] for x in open('input.txt').readlines() if x]

def get_adjacent(matrix, i, j):
    points = []
    if i+1 != len(matrix):
        points.append(matrix[i+1][j])
    if i != 0:
        points.append(matrix[i-1][j])
    if j+1 != len(matrix[i]):
        points.append(matrix[i][j+1])
    if j != 0:
        points.append(matrix[i][j-1])

    return points

def risk(points):
    return sum([p + 1 for p in points])


# Part 1
low_points = []
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        adj = get_adjacent(data, i, j)
        point = data[i][j]
        if all(a > point for a in adj):
            low_points.append(point)

print(risk(low_points))

# Part 2
def flood(mat, i, j, bas):
    if (i, j) in bas:
        return
    if mat[i][j] == 9:
        return

    bas.add((i,j))

    if i+1 != len(mat):
        flood(mat, i+1, j, bas)
    if i != 0:
        flood(mat, i-1, j, bas)
    if j+1 != len(mat[i]):
        flood(mat, i, j+1, bas)
    if j != 0:
        flood(mat, i, j-1, bas)

    return

def basin(matrix, i, j):
    bas = set()
    flood(matrix, i, j, bas)
    return bas

low_points = []
basins = []
for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        adj = get_adjacent(data, i, j)
        point = data[i][j]
        if all(a > point for a in adj):
            low_points.append(point)
            basins.append(basin(data, i, j))

basin_sizes = [len(b) for b in basins]
import functools
print(functools.reduce(lambda x, y: x * y, sorted(basin_sizes, reverse=True)[:3]))


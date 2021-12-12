data = [[int(y) for y in x.strip()] for x in open('input.txt').readlines() if x]
mat = data
total = 0


def pp(matrix):
    for row in matrix:
        print(row)

def tick(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] += 1

def flash(mat, i, j):
    if mat[i][j] == 0:
        return
    if mat[i][j] < 9:
        mat[i][j] += 1
        return
    
    global total
    total += 1
    # Update the point itself
    mat[i][j] = 0

    # Left col
    if i != 0:
        # Left
        flash(mat, i-1, j)
        # Up
        if j != 0:
            flash(mat, i-1, j-1)
        # Down
        if j+1 != len(mat[i]):
            flash(mat, i-1, j+1)

    # Right col
    if i+1 != len(mat):
        # Right
        flash(mat, i+1, j)
        # Up
        if j != 0:
            flash(mat, i+1, j-1)
        # Down
        if j+1 != len(mat[i]):
            flash(mat, i+1, j+1)

    # Up
    if j != 0:
        flash(mat, i, j-1)

    # Down
    if j+1 != len(mat[i]):
        flash(mat, i, j+1)


def flasher(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 10:
                flash(mat, i, j)

for step in range(100):
    tick(mat)
    flasher(mat)

print(total)

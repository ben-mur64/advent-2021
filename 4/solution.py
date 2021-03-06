data = [x.rstrip() for x in open('input.txt').readlines() if x]
data = filter(None, data)

nums = [int(x) for x in data[0].split(',')]

boards = []
for i in range(1, len(data) - 1, 5):
    board = [[int(x) for x in y.split()] for y in data[i:i+5]]
    boards.append(board)

def mark(board, num):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == num:
                board[i][j] = 'x'

def score(board, num):
    total = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] != 'x':
                total += board[i][j]
    return total * num

def check(board, num):
    for row in board:
        if len(set(row)) == 1:
            return True, score(board, num)
        
    for col in zip(*board):
        if len(set(col)) == 1:
            return True, score(board, num)

    return False, 0

# Part 1
for num in nums:
    for board in boards:
        mark(board, num)
        win, val = check(board, num)
        if win:
            print(val)
            break
    else:
        continue
    break

# Part 2

win = False
val = 0
btr = []
for num in nums:
    for b in reversed(btr):
        boards.pop(b)
    if len(boards) == 0:
        print(val)
        exit()
    btr = []
    for i in range(len(boards)):
        mark(boards[i], num)
        win, val = check(boards[i], num)
        if win:
            btr.append(i)

data = [x.strip() for x in open('input.txt').readlines() if x]

mapping = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>',
    }

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    }

def score(fails):
    total = 0
    for fail in fails:
        total += scoring[fail]
    return total

# Part 1
failures = []
for row in data:
    stack = []
    for char in row:
        if char in mapping.keys():
            stack.append(char)
        else:
            opener = stack.pop()
            if mapping[opener] != char:
                #print('Expected %s, but found %s instead.' % (mapping[opener], char))
                failures.append(char)
                break

print(score(failures))

# Part 2
scoring_auto = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    }

def process(row):
    stack = []
    for char in row:
        if char in mapping.keys():
            stack.append(char)
        else:
            opener = stack.pop()
            if mapping[opener] != char:
                #print('Expected %s, but found %s instead.' % (mapping[opener], char))
                failures.append(char)
                return
    return stack

def scoreauto(auto):
    total = 0
    for char in auto:
        total *= 5
        total += scoring_auto[char]
    return total

failures = []
autos = []
for row in data:
    stack = process(row)

    auto = []
    while stack:
        auto.append(mapping[stack.pop()])
    if auto:
        autos.append(auto)

scores = [scoreauto(x) for x in autos]
print(sorted(scores)[int(len(scores)/2)])

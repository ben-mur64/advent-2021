data = [x.strip() for x in open('input.txt').readlines() if x]
print(data)

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

failures = []
for row in data:
    stack = []
    for char in row:
        if char in mapping.keys():
            stack.append(char)
        else:
            opener = stack.pop()
            if mapping[opener] != char:
                print('Expected %s, but found %s instead.' % (mapping[opener], char))
                failures.append(char)
                break

print(failures)
print(score(failures))

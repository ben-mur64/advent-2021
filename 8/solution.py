import collections

data = [x.strip() for x in open('input.txt').readlines() if x]
display = [x.split('|')[0].strip().split() for x in data]
out = [x.split('|')[1].strip().split() for x in data]

#print(data)
#print(display)
#print(out)

# Part 1
total = 0
for row in out:
    for digit in row:
        if len(digit) in [2,3,4,7]:
            total += 1

print(total)

# Part 2

# A bit representation of the input digits
def bitrep(digit):
    return [1 if x in list(digit) else 0 for x in ['a','b','c','d','e','f','g']]

# A bit representation of the input digits
def ele_and(a, b):
    return [x & y for x,y in zip(a,b)]

# Returns a map of ints to bit representations of the string pertaining to them
def solve(row):
    solution = {}

    # Easy digits first
    for val in row:
        if len(val) == 2:
            solution['1'] = set(val)
        elif len(val) == 3:
            solution['7'] = set(val)
        elif len(val) == 4:
            solution['4'] = set(val)
        elif len(val) == 7:
            solution['8'] = set(val)

    # Length 5 first
    for val in row:
        if len(val) == 5:
            if len(set(val).difference(solution['7'])) == 2:
                solution['3'] = set(val)
            elif len(set(val).intersection(solution['4'])) == 2:
                solution['2'] = set(val)
            else:
                solution['5'] = set(val)

    # Now Length 6
    for val in row:
        if len(val) == 6:
            if len(set(val).intersection(solution['5'])) == 4:
                solution['0'] = set(val)
            elif len(set(val).intersection(solution['1'])) == 2:
                solution['9'] = set(val)
            else:
                solution['6'] = set(val)

    return solution

def calc(row, mapping):
    string_num = ''
    for digit in row:
        for k, v in mapping.items():
            if v == set(digit):
                string_num += k
    return string_num


all_rows = [x + y for x,y in zip(display, out)]

total = 0
for i in range(len(all_rows)):
    mapping = solve(all_rows[i])
    total += int(calc(out[i], mapping))


print(total)

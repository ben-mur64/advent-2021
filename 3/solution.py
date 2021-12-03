# Converts bitarray to a uint
def shift(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

data = [[int(x) for x in y.strip()] for y in  open('input.txt').readlines() if y]

# Part 1
threshold = len(data) / 2
responses = map(sum, zip(*data))

gamma = shift([x > threshold for x in responses])
epsilon = shift([x < threshold for x in responses])

print(gamma)
print(epsilon)
print(gamma * epsilon)


# Part 2

def oxygen(data, i):
    threshold = float(len(data)) / 2
    if len(data) == 1:
        return data[0]
    mcarr = [int(x > threshold) for x in map(sum, zip(*data))]
    ties = [int(x == threshold) for x in map(sum, zip(*data))]
    if ties[i] == 1:
        newdata = [[x for x in y if y[i] == 1] for y in data]
    else:
        newdata = [[x for x in y if y[i] == mcarr[i]] for y in data]
        
    newdata = [x for x in newdata if x]
    return oxygen(newdata, i + 1)

def co2(data, i):
    threshold = float(len(data)) / 2
    if len(data) == 1:
        return data[0]
    print(len(data))
    print(threshold)
    print(map(sum, zip(*data)))
    lcarr = [int(x < threshold) for x in map(sum, zip(*data))]
    print(lcarr)
    ties = [int(x == threshold) for x in map(sum, zip(*data))]
    print(ties)
    if ties[i] == 1:
        newdata = [[x for x in y if y[i] == 0] for y in data]
    else:
        newdata = [[x for x in y if y[i] == lcarr[i]] for y in data]
        
    newdata = [x for x in newdata if x]
    return co2(newdata, i + 1)

oxy = shift(oxygen(data, 0))
co = shift(co2(data, 0))
print(oxy)
print(co)
print(oxy * co)

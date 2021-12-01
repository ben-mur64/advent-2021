data = [int(x) for x in open('input.txt').readlines()]

# Part 1
count0 = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        count0 += 1
print(count0)

# Part 2
count1 = 0
for i in range(1, len(data) - 2):
    sum0 = data[i-1] + data[i] + data[i+1]
    sum1 = data[i] + data[i+1] + data[i+2]
    if sum1 > sum0:
        count1 += 1
print(count1)

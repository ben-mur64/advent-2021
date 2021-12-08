data = [x.strip() for x in open('input.txt').readlines() if x]
display = [x.split('|')[0].strip() for x in data]
out = [x.split('|')[1].strip() for x in data]

#print(data)
#print(display)
#print(out)

# Part 1
total = 0
for row in out:
    digits = row.split()
    for digit in digits:
        length = len(digit)
        if length in [2,3,4,7]:
            total += 1

print(total)

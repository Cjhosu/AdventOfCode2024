left = []
right = []

with open('day_one_input') as file:
    for line in file:
       line = line.strip('\n')
       pair = line.split('   ')
       left.append(pair[0])
       right.append(pair[1])

total = 0
for n in range(len(left)):
    ele  = left[n]
    curcount = right.count(ele)
    total += int(ele) * curcount
print(total)

left.sort()
right.sort()

total = 0
for n in range(len(left)):
    total += abs(int(left[n]) - int(right[n]))
print(total)

for n in range(7):
    print(n)

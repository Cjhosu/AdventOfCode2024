unsafe_counter = 0
safe_counter = 0

def ascender(report):
    global unsafe_counter
    global safe_counter
    for index in range(1, len(report)):
        level = int(report[index])
        previous_level = int(report[index -1])
        if level < previous_level:
           unsafe_counter += 1
           return
        difference = abs(int(level) - int(previous_level))
        if difference == 0 or difference > 3:
           unsafe_counter += 1
           return
    safe_counter += 1

def descender(report):
    global unsafe_counter
    global safe_counter
    for index in range(1, len(report)):
        level = int(report[index])
        previous_level = int(report[index -1])
        if level > previous_level:
           unsafe_counter += 1
           return
        difference = abs(int(level) - int(previous_level))
        if difference == 0 or difference > 3:
           unsafe_counter += 1
           return
    safe_counter += 1

with open('day_two_input') as file:
    for line in file:
        line = line.strip()
        report = line.split(' ')
        if int(report[0]) < int(report[1]):
            ascender(report)
        elif int(report[0]) > int(report[1]):
            descender(report)

print(safe_counter)

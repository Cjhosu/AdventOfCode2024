unsafe_counter = 0
safe_counter = 0

def ascender(report, retry):
    global unsafe_counter
    global safe_counter
    print("ascender")
    print(report)
    for index in range(1, len(report)):
        level = int(report[index])
        previous_level = int(report[index -1])
        difference = abs(int(level) - int(previous_level))
        if level < previous_level or difference == 0 or difference > 3:
            if not retry:
               print("del meth")
               del report[index - 1]
               ascender(report, True)
            else:
                print("unsafe")
                unsafe_counter += 1
                return
            return
    print("safe")
    safe_counter += 1

def descender(report, retry):
    global unsafe_counter
    global safe_counter
    print("decender")
    print(report)
    for index in range(1, len(report)):
        level = int(report[index])
        previous_level = int(report[index -1])
        difference = abs(int(level) - int(previous_level))
        if level > previous_level or difference == 0 or difference > 3:
            if not retry:
               print("del meth")
               del report[index - 1]
               descender(report, True)
            else:
                print("unsafe")
                unsafe_counter += 1
                return
            return
    print("safe")
    safe_counter += 1

with open('day_two_input') as file:
    for line in file:
        line = line.strip()
        report = line.split(' ')
        if int(report[0]) < int(report[len(report) - 1]):
            ascender(report, False)
        elif int(report[0]) > int(report[len(report) - 1]):
            descender(report, False)

print(safe_counter)

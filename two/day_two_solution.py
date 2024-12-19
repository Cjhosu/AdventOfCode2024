safe_counter = 0


def is_safe(levels):
    increase = levels[len(levels) - 1] > levels[0]
    if increase:
        for i in range(1, len(levels)):
            diff = levels[i] - levels[i - 1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1, len(levels)):
            diff = levels[i] - levels[i - 1]
            if not -3 <= diff <= -1:
                return False
        return True


def is_really_safe(levels):
    if is_safe(levels):
        return True
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i+1:]):
            return True
    return False


with open('day_two_input') as file:
    for line in file:
        line = line.strip()
        report = line.split(' ')
        levels = [int(i) for i in report]
        safe_counter += is_really_safe(levels)

print(safe_counter)

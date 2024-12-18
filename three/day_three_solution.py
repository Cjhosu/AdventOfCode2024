import re

total = 0
with open('day_three_input') as file:
    for line in file:
        line = line.strip()
        reg_list = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for each in reg_list:
            just_num = each.strip("mul").strip("(").strip(")")
            nums = [int(i) for i in just_num.split(",")]
            total += (nums[0] * nums[1])

print(total)

total = 0
process = True
with open('day_three_input') as file:
    for line in file:
        line = line.strip()
        reg_list = re.findall("do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for each in reg_list:
            just_num = each.strip("mul").strip("(").strip(")")
            if str(each) == "do()":
                process = True
            elif str(each) == "don't()":
                process = False
            elif process:
                try:
                    nums = [int(i) for i in just_num.split(",")]
                    total += (nums[0] * nums[1])
                except:
                    pass

print(total)

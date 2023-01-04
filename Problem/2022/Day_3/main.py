def char_value(val: str):
    if val.islower():
        return abs(ord('a')-ord(val)-1)
    else:
        return abs(ord('A')-ord(val)-1) + 26


def part_1():
    total = 0

    for line in data:
        # divide in 2
        center = len(line)//2
        left_side = set(line[:center])
        right_side = set(line[center:])

        # common char, value
        common = left_side.intersection(right_side).pop()
        total += char_value(common)

    return total


def part_2():
    total = 0

    for i in range(0, len(data), 3):
        # 3 lines
        a = set(data[i])
        b = set(data[i+1])
        c = set(data[i+2])

        # common char, value
        common = a.intersection(b, c).pop()
        total += char_value(common)

    return total

# - - - - - - - - - - - - - - -


file_name = "example_input.txt"
file_name = "input.txt"


# Getting data
with open(file_name) as file:
    data = [i for i in file.read().strip().split("\n")]

print(f"\nPart-1: {part_1()}\n")
print(f"\nPart-2: {part_2()}\n")

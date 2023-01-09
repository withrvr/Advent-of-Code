from part1 import Part_1
from part2 import Part_2

file_name = "example_input.txt"
file_name = "other_input.txt"
file_name = "input.txt"

# Getting data
with open(file_name) as file:
    data = [line.strip() for line in file]

# for line in data:
#     print(line)


Part_1(data)
Part_2(data)

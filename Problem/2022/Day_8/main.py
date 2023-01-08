from part1 import Part_1
from part2 import Part_2

file_name = "input.txt"
file_name = "example_input.txt"

# Getting data
with open(file_name) as file:
    data = [list(line.strip()) for line in file]

# row, col length
row_len = len(data)
col_len = len(data[0])

# for line in data:
#     print(line)

# print(row_len)
# print(col_len)

Part_1(data, row_len, col_len)
Part_2(data, row_len, col_len)

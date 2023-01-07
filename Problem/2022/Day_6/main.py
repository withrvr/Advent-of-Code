def distinct_char(subroutine, distinct):
    for i in range(distinct, len(subroutine)):  # loop from distinct to last
        val = subroutine[i-distinct:i]  # sub-array
        unique = len(set(val))  # no of unique character

        # print(f"at: {i:2}, value: {val}, unique: {unique}")

        if unique == distinct:
            break
    else:
        # in case not found
        return -1

    # at what character we found the char
    return i


# - - - - - - - - - - - - - - -
file_name = "input.txt"
file_name = "example_input.txt"


# Getting data
with open(file_name) as file:
    for line in file:
        print(line := line.strip())

        print(f"Part_1: {distinct_char(line, 4)}")  # part 1
        print(f"Part_2: {distinct_char(line, 14)}\n")  # part 2

def print_stack_list(arr):
    for i in range(1, len(arr)):
        print(f"{i}: {arr[i]}")


def part_1(m, f, t):
    part_1_stack_list[t] = part_1_stack_list[t] + \
        part_1_stack_list[f][-1:-1-m:-1]  # imp
    part_1_stack_list[f] = part_1_stack_list[f][:-m]


def part_2(m, f, t):
    part_2_stack_list[t] = part_2_stack_list[t] + \
        part_2_stack_list[f][-m:]  # imp
    part_2_stack_list[f] = part_2_stack_list[f][:-m]


# ---

file_name = "example_input.txt"
file_name = "input.txt"


# Getting data
with open(file_name) as file:
    graph = []
    moves = []

    # stack at starting
    while line := file.readline():
        if (line == "\n"):
            break
        else:
            graph.append(line)

    # n empty stack_list
    stack_list = [list() for _ in range(len(graph[0])//4)]

    # converting graph into stack_list
    for line in graph[-2::-1]:
        for i in range(0, len(graph[0]), 4):
            if (val := line[i+1]) != " ":
                stack_list[i//4].append(val)

    stack_list.insert(0, [])

    part_1_stack_list = stack_list[:]
    part_2_stack_list = stack_list[:]

    # not: moves to follow
    while move := file.readline():
        move = move.split()
        m = int(move[1])  # move
        f = int(move[3])  # from
        t = int(move[5])  # to

        # print_stack_list(part_2_stack_list)
        # print(f"{f} --> {t}, ({m})\n")

        part_1(m, f, t)
        part_2(m, f, t)

    # print_stack_list(part_2_stack_list)

    # results
    result_part_1 = "".join([stack[-1] for stack in part_1_stack_list[1:]])
    result_part_2 = "".join([stack[-1] for stack in part_2_stack_list[1:]])
    print(f"Part 1: {result_part_1}")
    print(f"Part 2: {result_part_2}")

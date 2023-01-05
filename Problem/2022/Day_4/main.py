def main():
    fully_contain = 0
    nothing_contain = 0
    half_contain = 0

    for line in data:
        a, b = line.split(",")

        a_start, a_end = map(int, a.split("-"))
        b_start, b_end = map(int, b.split("-"))

        if (a_start >= b_start and a_end <= b_end) or (b_start >= a_start and b_end <= a_end):
            fully_contain += 1
            print("1", end="")
        elif (a_end < b_start) or (b_end < a_start):
            nothing_contain += 1
            print("0", end="")
        else:
            half_contain += 1
            print("½", end="")

        print(f" : {line}")

    # overlap = len(data) - nothing_contain # can do like this also
    overlap = half_contain + fully_contain

    print("\nwhole_data:", len(data))
    print()
    print("(Part-1): fully_contain:", fully_contain)
    print("(Part-2): overlap:", overlap)
    print()
    print("nothing_contain:", nothing_contain)
    print("half_contain:", half_contain)

# - - - - - - - - - - - - - - -


file_name = "example_input.txt"
file_name = "input.txt"


# Getting data
with open(file_name) as file:
    data = [line.strip() for line in file]

main()

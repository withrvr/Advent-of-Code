with open("./1/input.txt", "r") as input_file:
	global lines
	lines = input_file.readlines()

# making str input to tuple pair
# & making colum list
arr = []
first = []
second = []

for line in lines:
	t_line = tuple(int(num) for num in line.strip().split())
	arr.append(t_line)

	first.append(t_line[0])
	second.append(t_line[1])


# some var
n = len(arr)
diff_sum = 0


# main logic
first.sort()
second.sort()

# for i in range(10):
# 	print(first[i], second[i])

for i in range(n):
	diff_sum += abs(first[i] - second[i])

print(diff_sum)

# with open("./1/sample.txt", "r") as input_file:
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


# --- main code ---

# some var
# diff_sum = 0
n = len(arr)
similarity_score = 0
dp = {} # for repeated values

# no need to sort now
# first.sort()
# second.sort()


# logic
for val in first:
	if val in dp:
		pass
	else:
		score = second.count(val) * val
		dp[val] = score

	# print(score)
	similarity_score += dp[val]

print(similarity_score)

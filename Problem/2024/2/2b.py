"""
without: index which we dont have to use

return

True: safe
False: unsafe
"""
def check_report(row=tuple(), without=None): # slope=None
	n = len(row)
	if n < 3:
		return True


	inc = True
	dec = True

	last = None

	if without == 0:
		last = row[1]
	else:
		last = row[0]

	# logic
	start = 2 if without == 0 else 1
	for i in range(start, n):
		if i == without:
			continue

		diff = row[i] - last

		# if slope == "inc":
		if diff <= 0 or diff > 3: # only 1 2 3 is allowed
			inc = False

		# elif slope == "dec":
		if diff >= 0 or diff < -3: # only -3 -2 -1 is allowed
			dec = False

		last = row[i]

	return inc or dec


# -------------------------- START FROM HERE --------------------------

if __name__ == "__main__":

	# with open("./2/sample.txt", "r") as input_file:
	with open("./2/input.txt", "r") as input_file:
		global lines
		lines = input_file.readlines()

	# making str input to tuple arr list
	arr = []
	safe = 0
	# un_safe = 0

	# looping through each line
	for line in lines:
		# converting to tuple
		row = tuple(int(val) for val in line.strip().split())
		n = len(row)

		arr.append(row) # adding row


		# logic

		result = False
		# trying without each element
		for i in range(n):
			result = check_report(row, without=i)
			if result:
				safe += result
				break

		print(f"row'{len(arr)} : {result} ..... cnt:{safe}")

	print()
	print(f"safe --> {safe}")
	print(f"unsafe --> {len(arr)-safe}")

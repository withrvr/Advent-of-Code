"""
return

True: safe
False: unsafe
"""
def check_report(row=tuple()): # slope=None
	n = len(row)
	if n < 3:
		return True


	inc = True
	dec = True

	# logic
	for i in range(1, n):
		diff = row[i] - row[i-1]

		# if slope == "inc":
		if diff <= 0 or diff > 3: # only 1 2 3 is allowed
			inc = False

		# elif slope == "dec":
		if diff >= 0 or diff < -3: # only -3 -2 -1 is allowed
			dec = False

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
		# if n < 3:
		# 	safe += 1
		# else:
		safe += check_report(row)

		# print(f"{len(arr)} ... {safe}")
		# print(un_safe)

	print(f"safe --> {safe}")
	print(f"unsafe --> {len(arr)-safe}")

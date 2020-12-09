# Day 09 - Part 2
print "Day 09 - Part 2"

with open("./day09-input.txt") as f:
	content = f.read().splitlines()

try:
	numbers = [int(number_as_string) for number_as_string in content]
except TypeError as e:
	print "Something was not a number"
	raise e


INVALID_NUMBER = 105950735


def sum_min_and_max_from_list(list_of_numbers):
	return min(list_of_numbers) + max(list_of_numbers)

i = 0
size = 1

while (i < len(numbers)):
	currenty_subarray = numbers[i:i+size]
	current_sum = sum(currenty_subarray)

	print i, size
	if current_sum == INVALID_NUMBER:
		print sum_min_and_max_from_list(currenty_subarray)
		break

	if current_sum < INVALID_NUMBER:
		size += 1
	else:
		i += 1
		size = 1

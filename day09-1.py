# Day 09 - Part 1
print "Day 09 - Part 1"

with open("./day09-input.txt") as f:
	content = f.read().splitlines()

try:
	numbers = [int(number_as_string) for number_as_string in content]
except TypeError as e:
	print "Something was not a number"
	raise e


PREAMBLE_SIZE = 25


def get_possible_values(preamble_start):
	return [
		numbers[preamble_start + i] + numbers[preamble_start + j]
		for i in xrange(PREAMBLE_SIZE)
		for j in xrange(i + 1, PREAMBLE_SIZE)
	]


for i in xrange(25, len(numbers)):
	possible_values = get_possible_values(i - 25)

	if numbers[i] not in possible_values:
		print possible_values
		print i
		print numbers[i]
		break

# Day 01 - Problem 1
print "Day 01 - Problem 1"

with open("./day01input.txt") as f:
	content = f.read().splitlines()

try:
	numbers = [int(number_as_string) for number_as_string in content]
except TypeError as e:
	print "Something was not a number"
	raise e

count_of_numbers = len(numbers)

for i in xrange(count_of_numbers):
	for j in xrange(i, count_of_numbers):
		if numbers[i] + numbers[j] == 2020:
			print numbers[i], numbers[j], numbers[i] * numbers[j]

# Day 10 - Part 1
print "Day 10 - Part 1"

with open("./day10-input.txt") as f:
	content = f.read().splitlines()

try:
	numbers = [int(number_as_string) for number_as_string in content]
except TypeError as e:
	print "Something was not a number"
	raise e


# Append device
numbers.append(max(numbers) + 3)


numbers.sort()


print content
print numbers


increment1 = 0
increment3 = 0
prev = 0 # This will add the outlet


for number in numbers:
	increment = number - prev
	if increment == 1:
		increment1 += 1
	elif increment == 3:
		increment3 += 1
	prev = number


print increment1, increment3, increment1 * increment3

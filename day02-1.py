# Day 02 - Part 1
print "Day 02 - Part 1"


with open("./day02-input.txt") as f:
	content = f.read().splitlines()


def parse_policy(policy):
	splitted_policy = policy.split("-")
	min_times = int(splitted_policy[0])
	max_times = int(splitted_policy[1].split()[0])
	letter = splitted_policy[1].split()[1]

	return min_times, max_times, letter


def check_password(policy, password):
	min_times, max_times, letter = parse_policy(policy)
	actual_count = password.count(letter)
	return min_times <= actual_count and actual_count <= max_times


count = 0


for entry in content:
	policy, password = entry.split(": ")
	if check_password(policy, password):
		count += 1
		print policy, password


print "There are {} valid passwords".format(count)

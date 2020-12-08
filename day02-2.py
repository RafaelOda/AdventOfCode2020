# Day 02 - Part 2
print "Day 02 - Part 2"


with open("./day02-input.txt") as f:
	content = f.read().splitlines()


def parse_policy(policy):
	splitted_policy = policy.split("-")
	first_position = int(splitted_policy[0])
	second_position = int(splitted_policy[1].split()[0])
	letter = splitted_policy[1].split()[1]

	return first_position, second_position, letter


def check_password(policy, password):
	first_position, second_position, letter = parse_policy(policy)
	password_length = len(password)

	if password_length < first_position:
		return False

	first_postion_has_letter = password[first_position - 1] == letter

	if password_length < second_position:
		return first_postion_has_letter

	second_position_has_letter = password[second_position - 1] == letter

	return first_postion_has_letter !=  second_position_has_letter


count = 0


for entry in content:
	policy, password = entry.split(": ")
	if check_password(policy, password):
		count += 1
		print policy, password


print "There are {} valid passwords".format(count)

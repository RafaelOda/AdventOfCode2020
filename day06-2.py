# Day 06 - Part 2
print "Day 06 - Part 2"

with open("./day06-input.txt") as f:
	content = f.read().splitlines()


count_for_every_group = 0
group_answers = list()


def count_for_current_group():
	if not group_answers:
		return

	number_of_common_answers = len(group_answers[0].intersection(*group_answers[1:]))
	return number_of_common_answers


for entry in content:
	if not entry:
		count_for_every_group += count_for_current_group()
		group_answers = list()
	else:
		group_answers.append(set(list(entry)))

count_for_every_group += count_for_current_group()


print count_for_every_group

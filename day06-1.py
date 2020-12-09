# Day 06 - Part 1
print "Day 06 - Part 1"

with open("./day06-input.txt") as f:
	content = f.read().splitlines()


group_answers = set()
every_group_answer = [group_answers]


for entry in content:
	group_answers = group_answers | set(list(entry))

	if not entry:
		every_group_answer.append(group_answers)
		group_answers = set()

every_group_answer.append(group_answers)

count_of_answers = [len(answers) for answers in every_group_answer]
print sum(count_of_answers)

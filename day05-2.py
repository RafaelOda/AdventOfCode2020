# Day 05 - Part 2
print "Day 05 - Part 2"

with open("./day05-input.txt") as f:
	content = f.read().splitlines()


# F = 0
# B = 1

# L = 0
# R = 1

def parse_boarding_pass(raw_boarding_pass):
	boarding_pass = {}

	raw_row = raw_boarding_pass[:7]
	raw_column = raw_boarding_pass[7:]

	row = int(raw_row.replace("F", "0").replace("B", "1"), 2)
	column = int(raw_column.replace("L", "0").replace("R", "1"), 2)

	boarding_pass["row"] = row
	boarding_pass["column"] = column
	boarding_pass["id"] = row * 8 + column

	return boarding_pass


all_boarding_passes = [parse_boarding_pass(boarding_pass) for boarding_pass in content]
all_ids = [boarding_pass["id"] for boarding_pass in all_boarding_passes]

max_id = max(all_ids)


for possible_id in xrange(1, max_id):
	if possible_id not in all_ids:
		previous_id = possible_id - 1
		next_id = possible_id + 1
		if previous_id in all_ids and next_id in all_ids:
			print "Your seat is the one that has the id: {}".format(possible_id)

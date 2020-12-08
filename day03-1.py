# Day 03 - Part 1
print "Day 03 - Part 1"


with open("./day03-input.txt") as f:
	content = f.read().splitlines()


def has_tree(spot):
	if spot != "#" and spot != ".":
		raise ValueError("Unexpected character")
	return spot == "#"


def count_trees_in_slope(arboreal_map, right, down):
	trees_count = 0
	horizontal_position = 0
	horizontal_size = len(arboreal_map[0])

	# Down is not used so far, but we are keeping it since I guess it will
	# be important in part 2...
	for line in arboreal_map:
		if has_tree(line[horizontal_position]):
			trees_count += 1
		horizontal_position += right
		horizontal_position = horizontal_position % horizontal_size

	return trees_count


arboreal_map = [list(line) for line in content]
total_trees = count_trees_in_slope(arboreal_map, 3, 1)


print "You will encounter {} trees".format(total_trees)

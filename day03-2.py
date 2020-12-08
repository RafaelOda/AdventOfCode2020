# Day 03 - Part 2
print "Day 03 - Part 2"


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

	for vertical_position in xrange(0, len(arboreal_map), down):
		line = arboreal_map[vertical_position]
		if has_tree(line[horizontal_position]):
			trees_count += 1
		horizontal_position += right
		horizontal_position = horizontal_position % horizontal_size

	return trees_count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

arboreal_map = [list(line) for line in content]
solution = 1


for slope in slopes:
	right, down = slope
	trees_count = count_trees_in_slope(arboreal_map, right, down)
	print trees_count
	solution *= trees_count


print solution

# Day 07 - Part 1
print "Day 07 - Part 1"

with open("./day07-input.txt") as f:
	rules = f.read().splitlines()


contents_by_color = {}


def parse_rule(rule):
	# it ignores count of bags. Probably only useful in part 2.
	rule = rule[:-1]

	if not " bags contain " in rule:
		raise ValueError("Something unexpected is in this rule. You probably messed up.")

	color, contents = rule.split(" bags contain ")

	if contents == "no other bags":
		contents_by_color[color] = []
		return

	colors_it_contains = []
	contents = contents.split(", ")

	for content in contents:
		content_count, content_color_with_suffix = content.split(" ", 1)
		content_color = content_color_with_suffix.split(" bag")[0]
		colors_it_contains.append(content_color)

	contents_by_color[color] = colors_it_contains


def contains_shiny_gold(color):
	contents = contents_by_color[color]

	if not contents:
		return False

	if "shiny gold" in contents:
		return True

	for content in contents:
		if contains_shiny_gold(content):
			return True

	return False


colors_that_may_contain_shiny_gold = 0


for rule in rules:
	parse_rule(rule)


for color in contents_by_color:
	if contains_shiny_gold(color):
		colors_that_may_contain_shiny_gold += 1


print contents_by_color
print colors_that_may_contain_shiny_gold


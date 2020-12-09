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

	parsed_contents = []
	contents = contents.split(", ")

	for content in contents:
		content_count, content_color_with_suffix = content.split(" ", 1)
		content_color = content_color_with_suffix.split(" bag")[0]
		parsed_contents.append({"color": content_color, "count": int(content_count)})

	contents_by_color[color] = parsed_contents


def count_bags_a_color_contains(color):
	contents = contents_by_color[color]
	count = 0

	for content in contents:
		count += content["count"]
		count += count_bags_a_color_contains(content["color"]) * content["count"]

	return count


for rule in rules:
	parse_rule(rule)


print count_bags_a_color_contains("shiny gold")

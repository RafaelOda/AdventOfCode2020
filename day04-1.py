# Day 04 - Part 1
print "Day 04 - Part 1"

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

with open("./day04-input.txt") as f:
	content = f.read().splitlines()


fields =  ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
required_fields =  ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


class Passport(object):

	def __init__(self, data=None):
		for field in fields:
			setattr(self, field, None)
		if data:
			self.load_data(data)

	def load_data(self, data={}):
		for field, value in data.iteritems():
			setattr(self, field, value)

	def is_valid(self):
		for field in required_fields:
			if getattr(self, field) is None:
				return False
		return True


passports = []


def create_passport(data=None):
	new_passport = Passport(data)
	passports.append(new_passport)
	return new_passport


passport = create_passport()


def parse_data_from_line(line):
	entries = line.split()
	data = {}
	for entry in entries:
		field, value = entry.split(":")
		data[field] = value

	return data


for line in content:
	if line:
		data = parse_data_from_line(line)
		passport.load_data(data)
	else:
		passport = create_passport()


valid_passports = [passport for passport in passports if passport.is_valid()]

print "There are {} valid passports".format(len(valid_passports))

# Day 04 - Part 2
print "Day 04 - Part 2"

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


def _is_valid_year(year):
	if len(year) != 4:
		return False
	try:
		year = int(year)
	except TypeError as e:
		print year
		return False
	return True


def _is_valid_birth_year(birth_year):
	if not _is_valid_year(birth_year):
		return False

	birth_year = int(birth_year)

	return birth_year >= 1920 and birth_year <= 2002


def _is_valid_issue_year(issue_year):
	if not _is_valid_year(issue_year):
		return False

	issue_year = int(issue_year)

	return issue_year >= 2010 and issue_year <= 2020


def _is_valid_expiration_year(expiration_year):
	if not _is_valid_year(expiration_year):
		return False

	expiration_year = int(expiration_year)

	return expiration_year >= 2020 and expiration_year <= 2030


def _is_valid_height(height):
	if len(height) < 4:
		return False
	unit = height[-2:]
	number = height[:-2]
	if unit != "in" and unit != "cm":
		return False

	try:
		number = int(number)
	except ValueError as e:
		print e
		print height
		return False

	if unit == "cm":
		return number >= 150 and number <= 193

	return number >= 59 and number <= 76


def _is_valid_hair_color(hair_color):
	if len(hair_color) != 7:
		return False
	if hair_color[0] != "#":
		return False
	try:
		int(hair_color[1:], 16)
	except ValueError:
		return False

	return True


def _is_valid_eye_color(eye_color):
	valid_eye_colors = "amb blu brn gry grn hzl oth".split()
	return eye_color in valid_eye_colors


def _is_valid_passport_id(passport_id):
	if len(passport_id) != 9:
		return False

	try:
		int(passport_id)
	except ValueError:
		return False

	return True


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
		return (
			_is_valid_birth_year(self.byr) and
			_is_valid_issue_year(self.iyr) and
			_is_valid_expiration_year(self.eyr) and
			_is_valid_height(self.hgt) and
			_is_valid_hair_color(self.hcl) and
			_is_valid_eye_color(self.ecl) and
			_is_valid_passport_id(self.pid)
		)


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

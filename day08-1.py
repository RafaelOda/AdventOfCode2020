# Day 08 - Part 1
print "Day 08 - Part 1"

with open("./day08-input.txt") as f:
	instructions = f.read().splitlines()


def parse_instruction(instruction):
	command, value_as_string = instruction.split()
	return command, int(value_as_string)


class ProgramLoop(Exception):
	pass


class ProgramRunner(object):
	def __init__(self, instructions):
		self.executed_instructions = []
		self.acc = 0
		self.current_index = 0
		self.instructions = instructions

	def run(self):
		print "Running Handheld console program"

		if not self.instructions:
			print "You must feed me with instructions."
			return

		try:
			self._execute_next_instruction()
		except ProgramLoop:
			print "Found loop executing {}, {}".format(
				self.current_index, self.instructions[self.current_index]
			)
			print self.acc

	def _execute_next_instruction(self):
		self._check_loop()
		self.executed_instructions.append(self.current_index)

		instruction = self.instructions[self.current_index]
		command, value = parse_instruction(instruction)

		if command == "acc":
			self.acc += value

		if command == "jmp":
			self.current_index += value
		else:
			self.current_index += 1

		self._execute_next_instruction()

	def _check_loop(self):
		if self.current_index in self.executed_instructions:
			raise ProgramLoop


program_runner = ProgramRunner(instructions)
program_runner.run()

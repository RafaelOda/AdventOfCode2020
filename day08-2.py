# Day 08 - Part 2
print "Day 08 - Part 2"

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
		self.instructions = instructions
		self.debug_node_index = None

	def run(self):
		print "Running Handheld console program"

		if not self.instructions:
			print "You must feed me with instructions."
			return

		try:
			self._execute_instruction_by_index(0)
		except ProgramLoop as e:
			if self.debug_node_index is not None:
				self._exit_debug_mode()
			else:
				print "Something really unexpected happened :("
				raise e

		print "Success!"
		print "Acc value: {}".format(self.acc)
		print "Node debugged: {}".format(self.debug_node_index)

	def _execute_instruction_by_index(self, index, disable_debug=False):
		# Checks end
		if index >= len(self.instructions):
			return

		# Checks loop
		if index in self.executed_instructions:
			raise ProgramLoop

		self.executed_instructions.append(index)
		instruction = self.instructions[index]
		command, value = parse_instruction(instruction)

		if command == "acc":
			self.acc += value
			self._execute_instruction_by_index(index + 1, disable_debug=disable_debug)
			return

		if not disable_debug:
			self.debug_node_index = index

			if command == "jmp":
				command = "nop"
			else:
				command = "jmp"

		disable_debug = self.debug_node_index is not None

		if command == "jmp":
			self._execute_instruction_by_index(index + value, disable_debug=disable_debug)
		else:
			self._execute_instruction_by_index(index + 1, disable_debug=disable_debug)


	def _check_if_nop_change_would_instantly_lead_to_end(self, value):
		return value + self.current_index >= len(self.instructions) - 5

	def _exit_debug_mode(self):
		debug_node_index = self.debug_node_index
		self.debug_node_index = None
		self.executed_instructions = self.executed_instructions[
			: self.executed_instructions.index(debug_node_index)
		]
		self._execute_instruction_by_index(debug_node_index, disable_debug=True)


program_runner = ProgramRunner(instructions)
program_runner.run()

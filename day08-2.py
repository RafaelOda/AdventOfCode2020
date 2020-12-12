# Day 08 - Part 2
import sys

sys.setrecursionlimit(10000)

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
		self.temp_acc = 0
		self.instructions = instructions
		self.debug_node_index = None

	def run(self):
		print "Running Handheld console program"

		if not self.instructions:
			print "You must feed me with instructions."
			return

		self._execute_instruction_by_index(0)

		print "Success!"
		print "Acc value: {}".format(self.acc)
		print "Node debugged: {}".format(self.debug_node_index)

	def _execute_instruction_by_index(self, index, force_disable_debug=False):
		# Checks end
		if index >= len(self.instructions):
			return

		# Checks loop
		if index in self.executed_instructions:
			if self.debug_node_index is not None:
				self._exit_debug_mode()
				return
			else:
				raise ProgramLoop("Something really strange happened")

		self.executed_instructions.append(index)
		instruction = self.instructions[index]
		command, value = parse_instruction(instruction)

		if command == "acc":
			self.acc += value
			self._execute_instruction_by_index(index + 1)
			return

		if not force_disable_debug and self.debug_node_index is None:
			self._enter_debug_mode(index)

			if command == "jmp":
				command = "nop"
			else:
				command = "jmp"

		if command == "jmp":
			self._execute_instruction_by_index(index + value)
		else:
			self._execute_instruction_by_index(index + 1)


	def _check_if_nop_change_would_instantly_lead_to_end(self, value):
		return value + self.current_index >= len(self.instructions) - 5

	def _enter_debug_mode(self, index):
			print "Entering debug mode for index {}".format(index)
			self.debug_node_index = index
			self.temp_acc = self.acc

	def _exit_debug_mode(self):
		print "Exiting debug mode for node {}".format(self.debug_node_index)
		debug_node_index = self.debug_node_index
		self.debug_node_index = None
		self.executed_instructions = self.executed_instructions[
			: self.executed_instructions.index(debug_node_index)
		]
		self.acc = self.temp_acc
		self._execute_instruction_by_index(debug_node_index, force_disable_debug=True)


program_runner = ProgramRunner(instructions)
program_runner.run()

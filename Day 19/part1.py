import json

class Workflow:

	workflows= {}

	def __init__(self, workflow_string):
		self.name, func_strings = workflow_string.split('{')
		func_strings = func_strings.replace('}', '')
		func_strings = func_strings.split(',')
		self.funcs = list(map(self.generate_func, func_strings))
		Workflow.workflows[self.name] = self


	def generate_func(self, func_string):
		if not ':' in func_string:
			return lambda x: func_string

		expression, result = func_string.split(':')
		
		if '<' in expression:
			variable, value = expression.split('<')
			return lambda x: result if x[variable] < int(value) else None

		if '>' in expression:
			variable, value = expression.split('>')
			return lambda x: result if x[variable] > int(value) else None

	def run_workflow(self, part):
		for f in self.funcs:
			res = f(part)
			if res in ('R', 'A'):
				return res

			if res is None:
				continue

			return Workflow.workflows[res].run_workflow(part)

def parse_part(part):
	part = part.replace('{', '').replace('}', '')
	return {x.split('=')[0]: int(x.split('=')[1]) for x in part.split(',')}

with open('input.txt', 'r') as file:
	input_data = file.read()

workflows, raw_parts = input_data.split('\n\n')
for workflow in workflows.split('\n'):
	Workflow(workflow)

parts = [parse_part(part) for part in raw_parts.split('\n')[:-1]]

total = 0
for part in parts:
	res =  Workflow.workflows['in'].run_workflow(part)
	if res == 'A':
		total += sum(part.values())

print(total)








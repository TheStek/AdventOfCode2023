import re

with open('input.txt') as f:
	lines = f.readlines()

def get_calibration_value(text):
	numbers = re.findall(r'(\d)', text)
	return int(''.join([numbers[0], numbers[-1]]))

print(sum(map(get_calibration_value, lines)))

number_text = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
number_map = {text: str(i) for (i, text) in enumerate(number_text)}

def get_calibration_value_2(text):
	def get_map_value(x):
		try:
			return number_map[x]
		except KeyError:
			return x
	
	number_group =r'(\d|' + '|'.join(number_text) + ')'
	first = re.findall(rf'^.*?{number_group}.*$', text)[0]
	last = re.findall(rf'^.*{number_group}.*?$', text)[0]

	return int(get_map_value(first) + get_map_value(last))

print(sum(map(get_calibration_value_2, lines)))
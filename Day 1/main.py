import re

with open('input.txt') as f:
	lines: list[str] = f.readlines()

def get_calibration_value(text: str) -> int:
	numbers: list[str] = re.findall(r'(\d)', text)
	return int(''.join([numbers[0], numbers[-1]]))

print(sum(map(get_calibration_value, lines)))

number_text: list[str] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_map: dict[str, str] = {text: str(i) for (i, text) in enumerate(number_text)}

def get_calibration_value_2(text: str) -> int:
	def get_map_value(x: str) -> str:
		try:
			return number_map[x]
		except KeyError:
			return x

	number_group: str = r'(\d|' + '|'.join(number_text) + ')'
	first: str = re.findall(rf'^.*?{number_group}.*$', text)[0]
	last: str = re.findall(rf'^.*{number_group}.*?$', text)[0]

	return int(get_map_value(first) + get_map_value(last))

print(sum(map(get_calibration_value_2, lines)))
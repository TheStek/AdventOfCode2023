from copy import deepcopy

test = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

def parse_input(inp):
	return list(map(list, inp.split('\n')[:-1]))

def reorient(plat):
	return [[*x] for x in zip(*plat)]


def tilt_north(plat):
	oriented = reorient(deepcopy(plat))
	for r in range(len(oriented)):
		splits = ''.join(oriented[r]).split('#')
		tilted = '#'.join(list(map(lambda x: ''.join(sorted(x, reverse = True)), splits)))
		oriented[r] = list(tilted)
	return reorient(oriented)


def get_total_load(plat):
	l = len(plat)
	load = 0
	for i, row in enumerate(plat):
		load += len(list(filter(lambda x: x=='O', row))) * (l - i)
	return load



with open('input.txt', 'r') as file:
		input_data = file.read()

for row in parse_input(input_data):
	print(*row, sep = '')

print('\n\n')

for row in tilt_north(parse_input(input_data)):
	print(*row, sep = '')

print(get_total_load(tilt_north(parse_input(input_data))))
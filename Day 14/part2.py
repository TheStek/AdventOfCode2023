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


def tilt_south(plat):
	oriented = reorient(deepcopy(plat))
	for r in range(len(oriented)):
		splits = ''.join(oriented[r]).split('#')
		tilted = '#'.join(list(map(lambda x: ''.join(sorted(x, reverse = False)), splits)))
		oriented[r] = list(tilted)
	return reorient(oriented)


def tilt_east(plat):
	plat = deepcopy(plat)
	for r in range(len(plat)):
		splits = ''.join(plat[r]).split('#')
		tilted = '#'.join(list(map(lambda x: ''.join(sorted(x, reverse = True)), splits)))
		plat[r] = list(tilted)
	return plat


def tilt_west(plat):
	plat = deepcopy(plat)
	for r in range(len(plat)):
		splits = ''.join(plat[r]).split('#')
		tilted = '#'.join(list(map(lambda x: ''.join(sorted(x, reverse = False)), splits)))
		plat[r] = list(tilted)
	return plat

def get_total_load(plat):
	l = len(plat)
	load = 0
	for i, row in enumerate(plat):
		load += len(list(filter(lambda x: x=='O', row))) * (l - i)
	return load

def run_cycle(plat):
	plat = tilt_north(plat)
	plat = tilt_west(plat)
	plat = tilt_south(plat)
	plat = tilt_east(plat)
	return plat, get_total_load(plat)


with open('input.txt', 'r') as file:
		input_data = file.read()

loads = [-1, -1]
counter = 0
plat = parse_input(input_data)
while counter < 1_000_000_000:
	if counter % 10_000 == 0:
		print(counter)
	counter += 1
	plat, load = run_cycle(plat)
	if load == loads[-1] and load == loads[-2]:
		print(load, counter)
		break
	loads.append(load)
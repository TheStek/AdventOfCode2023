


direction_map = {'L': (0, -1),
	'R': (0, 1),
	'U': (-1, 0),
	'D': (1, 0)}


def parse_input(inp):
	def parse_line(line):
		direction, num, colour = line.split(' ')
		return (direction, int(num))
	return list(map(parse_line, inp))


def add_vectors(v1, v2):
	return tuple(v1[i] + v2[i] for i in range(len(v1)))

def dig_trench(direction, distance, current_loc):
	trench_locs = []
	direction_vec = direction_map[direction]
	for i in range(distance):
		current_loc = add_vectors(current_loc, direction_vec)
		trench_locs.append(current_loc)
	return trench_locs


def translate_origin(trench_locs):
	min_row = min(map(lambda x: x[0], trench_locs))
	min_col = min(map(lambda x: x[1], trench_locs))
	new_locs = []

	new_locs = list(map(lambda x: add_vectors(x, (-1*min_row, -1*min_col)), trench_locs))
	return new_locs


def print_trenches(trench_locs):
	max_row = max(map(lambda x: x[0], trench_locs))
	max_col = max(map(lambda x: x[1], trench_locs))
	for i in range(max_row + 1):
		for j in range(max_col + 1):
			if (i, j) in trench_locs:
				print('#', end = '')
			else:
				print('.', end = '')
		print()
	print('\n\n')


def fill_lake(trench_locs):
	lake = []
	max_row = max(map(lambda x: x[0], trench_locs))
	max_col = max(map(lambda x: x[1], trench_locs))
	for i in range(max_row + 1):
		in_lake = False
		for j in range(max_col + 1):
			if i==2:
					print(i, j, in_lake)
			if (i, j) in trench_locs:
				lake.append((i, j))
				# want to flip in_lake at the outside edge
				
				if ((i, j+1) not in trench_locs):
					in_lake = not in_lake
					continue
			else:
				if in_lake:
					lake.append((i, j))
	return lake


test = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split('\n')


with open('input.txt', 'r') as file:
	input_data = file.read().split('\n')[:-1]


dig_instructions = parse_input(input_data)

trenches_dug = [(0, 0)]
for ins in dig_instructions:
	trenches_dug.extend(dig_trench(*ins, trenches_dug[-1]))


trenches_dug = translate_origin(trenches_dug)

# print_trenches(trenches_dug)

lake = fill_lake(trenches_dug)

print(len(lake))

# print_trenches(lake)



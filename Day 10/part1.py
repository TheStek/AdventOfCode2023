with open('input.txt', 'r') as file:
	input_data = file.read().split('\n')[:-1]

test_input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".split('\n')

connection_map = {
	'|': [(-1, 0), (1, 0)],
	'-': [(0, -1), (0, 1)],
	'L': [(-1, 0), (0, 1)],
	'J': [(-1, 0), (0, -1)],
	'7': [(1, 0), (0, -1)],
	'F': [(1, 0), (0, 1)],
	'S': [ (-1, 0), (0, -1), (0, 1), (1, 0)]
}



def parse_input(inp):
	s_loc = None
	max_row = len(inp) - 1
	connection_grid = [[None for x in range(len(inp[i]))] for i in range(len(inp))]
	for r in range(max_row + 1):
		max_col = len(inp[r]) - 1
		for c in range(max_col + 1):
			connections = []

			directions = connection_map.get(inp[r][c])

			if not directions:
				continue

			if inp[r][c] == 'S':
				s_loc = (r, c)

			for direction in directions:
				dest = (r+direction[0], c+direction[1])
				if dest[0] < 0 or dest[1] < 0 or dest[0]> max_row or dest[1] > max_col:
				
					continue
				connections.append(dest)

			if len(connections) == 2 or inp[r][c] == 'S':
				connection_grid[r][c] = connections

	return connection_grid, s_loc


# Make sure path = [S, start]
def walk_along_path(path, gmap):
	loop = True
	path = path.copy()
	while loop:

		possible_next_moves = gmap.get(path[-1])
		if possible_next_moves is None:
			return

		# print(f'Currently at {path[-1]}, possible next = {possible_next_moves}')

		for move in possible_next_moves:
			if move != path[-2]:
				path.append(move)
				break

		if path[-1] == path[0]:
			# print(f'Finished - {path}')
			loop = False
	return path



def change_grid_to_map(grid):
	gmap = {}
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c]:
				gmap[(r, c)] = grid[r][c]
	return gmap


grid, s_loc = parse_input(input_data)

gmap = change_grid_to_map(grid)


paths = [[s_loc, x] for x in grid[s_loc[0]][s_loc[1]]]
final_walk = None
for path in paths:
	walk = walk_along_path(path, gmap)
	final_walk = walk
	if walk:
		print((len(walk) - 1) / 2)
print(len(final_walk))
final_walk.sort()

walk_details = {row: list(map(lambda x: x[1], filter(lambda x: x[0] == row, final_walk))) for row in set(map(lambda x: x[0], final_walk))}

import itertools

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda pair: pair[1] - pair[0]):
        b = list(b)
        yield b[0][1], b[-1][1]


print(list(ranges([1, 2, 3, 4, 59, 71,72])))





def get_enclosed_in_row(length, loopcells):
	if not loopcells:
		return 0
	enclosed = False
	total_enclosed = 0
	for i in range(length):
		if i in loopcells:
			if i+1 in loopcells:
				continue
			if i-1 not in loopcells:
				enclosed = not enclosed

			continue

		if enclosed:
			print(f'{i} is enclosed')
			total_enclosed += 1

	return total_enclosed

print(get_enclosed_in_row(5, [0, 1,3,  4]))


total = 0
for row, items in walk_details.items():
	total += get_enclosed_in_row(len(input_data[row]), items)
print(total)
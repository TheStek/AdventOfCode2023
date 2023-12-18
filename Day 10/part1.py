with open('input.txt', 'r') as file:
	input_data = list(map(list, file.read().split('\n')[:-1]))

test_input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ""".split('\n')

connection_map = {
	'|': [(-1, 0), (1, 0)], # north south
	'-': [(0, -1), (0, 1)], # east west
	'L': [(-1, 0), (0, 1)], # north east
	'J': [(-1, 0), (0, -1)], # north west
	'7': [(1, 0), (0, -1)], # # west south
	'F': [(1, 0), (0, 1)], # east south
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
print(s_loc, final_walk[1], final_walk[-2])
final_walk.sort()

walk_details = {row: list(map(lambda x: x[1], filter(lambda x: x[0] == row, final_walk))) for row in set(map(lambda x: x[0], final_walk))}


"""alfonsusac

Basically the pseudocode is:
for each row, let isInside = false.
for each char in row,
if its a ┌ or └, remember this curve.
if its a ┐ and previous curve is ┌ (forming ┌┐), then forget previous curve
if its a ┘ and previous curve is └ (forming └┘), then forget previous curve
if its a ┐and previous curve is └ (forming └┐), then its a barrier and flip isInside flag
if its a ┘and previous curve is ┌ (forming ┌┘), then its a barrier and flip isInside flag
then if its a pipe that doesn't have a distance (not part of the loop) and the isInside flag is true, you can just count it as insideSpace"""
def get_enclosed_in_row(row, inp, loop_cells, length):
	enclosed = False
	previous_curve = None
	enclosed_cells = 0
	for i in range(length):
		if i not in loop_cells:
			if enclosed:
				enclosed_cells += 1
			continue
		if inp[row][i] in ('FL'):
			previous_curve = inp[row][i]
			continue

		if inp[row][i] == '7' and previous_curve == 'F':
			previous_curve = None
			continue

		if inp[row][i] == 'J' and previous_curve == 'L':
			previous_curve = None
			continue

		if inp[row][i] == '7' and previous_curve == 'L':
			enclosed = not enclosed
			continue

		if inp[row][i] == 'J' and previous_curve == 'F':
			enclosed = not enclosed
			continue
	return enclosed_cells


input_data[s_loc[0]][s_loc[1]] = 'F'
	
# S is an F

total = 0
for row, items in walk_details.items():
	total += get_enclosed_in_row(row, input_data, items, len(input_data[row]))
print(total)
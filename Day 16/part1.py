def add_vectors(v1, v2):
	return tuple(v1[i] + v2[i] for i in range(len(v1)))


def advance_beams(beams, grid):
	new_beams = []
	locs = []
	for loc, direction in beams:
		new_loc = add_vectors(loc, direction)
		
		
		if min(new_loc) < 0 or new_loc[0] >= len(grid) or new_loc[1] >= len(grid[0]):
			continue

		symbol = grid[new_loc[0]][new_loc[1]]
		locs.append(new_loc)
		
		if symbol == '.':
			new_beams.append((new_loc, direction))
			continue

		if symbol == '|':
			if direction[1] == 0:
				new_beams.append((new_loc, direction))
				continue

			else:
				new_beams.append((new_loc, (1, 0)))
				new_beams.append((new_loc, (-1, 0)))

		if symbol == '-':
			if direction[0] == 0:
				new_beams.append((new_loc, direction))
				continue

			else:
				new_beams.append((new_loc, (0, 1)))
				new_beams.append((new_loc, (0, -1)))
				continue

		if symbol == '\\':
			# left
			if direction == (0, 1):
				new_beams.append((new_loc, (1, 0)))

			# right
			elif direction == (0, -1):
				new_beams.append((new_loc, (-1, 0)))

			# down
			elif direction == (1, 0):
				new_beams.append((new_loc, (0, 1)))

			# up
			else:
				new_beams.append((new_loc, (0, -1)))
			continue


		if symbol == '/':
			if direction == (0, 1):
				new_beams.append((new_loc, (-1, 0)))

			elif direction == (0, -1):
				new_beams.append((new_loc, (1, 0)))

			elif direction == (1, 0):
				new_beams.append((new_loc, (0, -1)))

			else:
				new_beams.append((new_loc, (0, 1)))
			continue
	return new_beams, set(locs)

def print_visited(grid, visited):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (i, j) in visited:
				print('#', end = '')
			else:
				print('.', end = '')
		print()


if __name__ == '__main__':
	with open('input.txt', 'r') as file:
		input_data = file.read().split('\n')[:-1]



	test = r""".|...\....
	|.-.\.....
	.....|-...
	........|.
	..........
	.........\
	..../.\\..
	.-.-/..|..
	.|....-|.\
	..//.|....""".split('\n')

	beam_history = {}
	beams = [((0, -1), (0, 1))]
	visited = set()

	loop = True
	while loop:
		loop = False
		beams, new_locs = advance_beams(beams, input_data)
		only_new_beams = []
		for beam in beams:
			try:
				beam_history[beam]
			except KeyError:
				loop = True
				beam_history[beam] = 1
				only_new_beams.append(beam)
		beams = only_new_beams
		visited = visited.union(new_locs)

	print(len(visited))


	print(len(input_data))
	print(len(input_data[0]))
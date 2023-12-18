from part1 import advance_beams



def find_energised_cells(grid, starting_position):
	beam_history = {}
	beams = [starting_position]
	visited = set()

	loop = True
	while loop:
		loop = False
		beams, new_locs = advance_beams(beams, grid)
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

	return len(visited)


def get_all_starting_positions(grid):
	rows = len(grid)
	cols = len(grid[0])

	positions = []

	# top row
	positions.extend([((-1, i), (1, 0)) for i in range(cols)])

	# left col
	positions.extend([((i, -1), (0, 1)) for i in range(rows)])

	# right col
	positions.extend([((i, cols), (0, -1)) for i in range(rows)])

	# bottom row
	positions.extend([((rows, i), (-1, 0)) for i in range(cols)])


	return set(positions)


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


pos = get_all_starting_positions(input_data)
scores = list(map(lambda x: find_energised_cells(input_data, x),pos))

print(list(zip(scores, pos)))
print(max(*scores))
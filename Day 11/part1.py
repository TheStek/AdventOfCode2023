with open('input.txt', 'r') as file:
	input_data = file.read().split('\n')[:-1]

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split('\n')


def parse_input(inp):
	rows = len(inp)
	cols = len(inp[0])
	galaxies = []
	for r in range(rows):
		for c in range(cols):
			if inp[r][c] == '#':
				galaxies.append([r, c])
	return rows, cols, galaxies

def expand_universe(rows, cols, galaxies):
	galaxies = galaxies.copy()

	rows_to_expand = list(set(range(rows)).difference(set(map(lambda x: x[0], galaxies))))
	cols_to_expand = list(set(range(rows)).difference(set(map(lambda x: x[1], galaxies))))

	empty_rows = []

	for i in range(len(galaxies)):
		added_rows = sum([1 if x < galaxies[i][0] else 0 for x in rows_to_expand])
		added_cols = sum([1 if x < galaxies[i][1] else 0 for x in cols_to_expand])
		galaxies[i][0] += added_rows
		galaxies[i][1] += added_cols


	return galaxies


def get_distance(g1, g2):
	return abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])

expanded_galaxies = expand_universe(*parse_input(input_data))

total = 0
for g1 in range(len(expanded_galaxies)):
	for g2 in range(len(expanded_galaxies)):
		if g1 < g2:
			dist = get_distance(expanded_galaxies[g1], expanded_galaxies[g2])
			total += dist
print(total)

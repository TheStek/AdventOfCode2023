

def parse_input(inp):
	return list(map(lambda x: x.split('\n'), inp))


def print_pattern(pattern):
	for row in pattern:
		if type(row) == str:
			print(row)
		else:
			print(''.join(row))
	print('\n')

def find_horizontal_reflections(pattern):
	for r1, r2 in zip(range(len(pattern)), range(1, len(pattern))):
		if pattern[r1] != pattern[r2]:
			continue
		reflection = True
		for i in range(1, min(r1 + 1, len(pattern) - r2)):
			if pattern[r1-i] != pattern[r2 + i]:
				reflection = False
				break

		if reflection:
			return r1, r2

def find_vertical_reflections(pattern):
	flipped = [*zip(*pattern)]
	return find_horizontal_reflections(flipped)


def get_reflection_score(pattern):
	total = 0
	h = find_horizontal_reflections(pattern)
	v = find_vertical_reflections(pattern)

	if h:
		total += (h[0] + 1) * 100
	if v:
		total += (v[0] + 1) * 1
	return total


if __name__ == '__main__':

	test = """#.##..##.
	..#.##.#.
	##......#
	##......#
	..#.##.#.
	..##..##.
	#.#.##.#.

	#...##..#
	#....#..#
	..##..###
	#####.##.
	#####.##.
	..##..###
	#....#..#""".split('\n\n')

	with open('input.txt', 'r') as file:
		input_data = file.read().split('\n\n')

	patterns = parse_input(input_data)

	print(sum(map(get_reflection_score, patterns)))

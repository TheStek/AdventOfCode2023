from part1 import *
from copy import deepcopy

def fix_smudge(pattern):
	pattern = list(map(list, pattern.copy()))
	orig_score = get_reflection_score(pattern)
	print(orig_score)
	print_pattern(pattern)
	for row in range(len(pattern)):
		print(row)
		for col in range(len(pattern[row])):
			new_pattern = deepcopy(pattern)
			if new_pattern[row][col] == '#':
				new_pattern[row][col] = '.'
			else:
				new_pattern[row][col] = '#'
			print_pattern(new_pattern)
			new_score = get_reflection_score(new_pattern)
			print(new_score)
			if new_score != orig_score:
				return new_score
	return 0



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

	patterns = parse_input(test)

	print(sum(map(fix_smudge, patterns)))
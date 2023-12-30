import numpy as np
from itertools import combinations


def parse_stone(stone):
	def convert_to_tuple(numstring):
		return tuple((int(x) for x in numstring.split(', ')))
	return tuple(map(convert_to_tuple, stone.split(' @ ')))

def find_intersection_point(p1, p2):
	M = np.matrix([[p1[1][0], -1*p2[1][0]],
		[p1[1][1], -1*p2[1][1]]])

	c = np.array([p2[0][0] - p1[0][0], p2[0][1] - p1[0][1]])

	try:
		t, s = np.linalg.solve(M, c)

		if min(t, s) < 0:
			return

		return np.array(p1[0]) + (t*np.array(p1[1]))

	except np.linalg.LinAlgError:
		return


test = '''19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3'''.split('\n')

with open('input.txt', 'r') as f:
	input_data = f.read().split('\n')[:-1]

data = map(parse_stone, input_data)

bounds = (200000000000000, 400000000000000)

crosses_in_boundary = 0

for c in combinations(data, 2):
	intersection_point = find_intersection_point(*c)
	if intersection_point is None:
		continue

	if intersection_point[0] < bounds[0] or intersection_point[0] > bounds[1]:
		continue

	if intersection_point[1] < bounds[0] or intersection_point[1] > bounds[1]:
		continue

	crosses_in_boundary += 1

print(crosses_in_boundary)
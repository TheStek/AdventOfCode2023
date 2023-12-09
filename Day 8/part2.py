from math import lcm

with open('input.txt', 'r') as file:
	input_data = file.read().split('\n')[:-1]

import re
test_input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split('\n')


direction_map = {'L': 0, 'R': 1}

def parse_input(inp):
	directions = inp[0]
	network = {}

	for line in inp[2:]:
		loc, left, right = re.findall(r'[A-Z\d]{3}', line)
		network[loc] = (left, right)
	return directions, network


def find_z_loops(starting_location, directions, network):
	z_loops = []
	keep_looping = True
	current_path_directions = []
	current_path = [starting_locations]
	current_location = starting_location
	step = 0
	while keep_looping:
		direction = directions[step % len(directions)]
		current_location = network[current_location][direction_map[direction]]
		current_path.append(current_location)
		current_path_directions.append(direction)
		if current_location[2] == 'Z':
			if [current_path_directions, current_path] in z_loops:
				keep_looping = False
			z_loops.append([current_path_directions, current_path])
			current_path = [current_location]
			current_path_directions = []
		step += 1
		

	return list(map(lambda x: len(x[1]), z_loops))


def follow_directions(directions, network):
	def get_new_location(d, l):
		return network[l][direction_map[d]]

	step = 0
	current_locations = list(filter(lambda x: x[2] == 'A', network.keys()))

	while list(filter(lambda x: x[2] != 'Z', current_locations)):

		direction = directions[step % len(directions)]
		current_locations = list(map(lambda x: get_new_location(direction, x), current_locations))
		step += 1

	return step


directions, network = parse_input(input_data)
starting_locations = list(filter(lambda x: x[2] == 'A', network.keys()))
z_loop_lengths = []
for starting_location in starting_locations:
	loop_lengths = find_z_loops(starting_location, directions, network)
	assert len(set(loop_lengths)) == 1, "Oh no"
	z_loop_lengths.append(loop_lengths[0]-1)

print(lcm(*z_loop_lengths))




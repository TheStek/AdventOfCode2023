with open('input.txt', 'r') as file:
	input_data = file.read().split('\n')[:-1]

import re
test_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split('\n')


direction_map = {'L': 0, 'R': 1}

def parse_input(inp):
	directions = inp[0]
	network = {}

	for line in inp[2:]:
		loc, left, right = re.findall(r'[A-Z]{3}', line)
		network[loc] = (left, right)
	return directions, network


def follow_directions(directions, network):
	step = 0
	current_location = 'AAA'
	location_history = ['AAA']

	while current_location != 'ZZZ':

		direction = directions[step % len(directions)]
		current_location = network[current_location][direction_map[direction]]
		location_history.append(current_location)
		step += 1

	return step, location_history

print(follow_directions(*parse_input(input_data)))



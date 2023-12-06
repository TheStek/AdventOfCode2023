with open('input.txt') as file:
	input_data = file.read()[:-1]
print(input_data)
test_input = """Time:      7  15   30
Distance:  9  40  200"""


def parse_data(inp):
	check_num = lambda x: all([y.isdigit() for y in x]) and x != ''
	deep_map_int = lambda x: list(map(int, x))
	time, distance =  list(map(deep_map_int, map(lambda x: list(filter(check_num, x)),
		map(lambda x: x.split(' '),inp.split('\n')))))
	return zip(time, distance)



def get_distance(X):
	x, t = X
	return x*(t-x)

def count_solutions(time, distance):
	setups = [(x, time) for x in range(time+1)]
	distances = map(get_distance, setups)
	return len(list(filter(lambda x: x>distance, distances)))

for time, distance in parse_data(input_data):
	print(count_solutions(time, distance))

def get_big_race(inp):
	time, distance = map(lambda x: int(''.join(list(filter(lambda y: y.isdigit(), x)))),inp.split('\n'))
	return time, distance

print(count_solutions(*get_big_race(input_data)))
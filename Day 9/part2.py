with open('input.txt', 'r') as file:
	input_data = file.read().split('\n')[:-1]

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split('\n')

def parse_input(inp):
	deep_map_int = lambda x: list(map(int, x))
	nums = list(map(lambda x: x.split(' '), inp))
	return list(map(deep_map_int, nums))

def get_differences(nums):
	return list(map(lambda x: x[1] - x[0], zip(nums, nums[1:])))

all_zeroes = lambda x: all([i == 0 for i in x])

def get_previous_value(nums):
	sequences = [nums]
	while not all_zeroes(sequences[-1]):
		sequences.append(get_differences(sequences[-1]))
	sequences.reverse()


	for i in range(len(sequences)-1):
		sequences[i+1].insert(0, sequences[i+1][0] - sequences[i][0])

	return sequences[-1][0]


print(get_previous_value(parse_input(test_input)[2]))

print(sum(map(get_previous_value, parse_input(input_data))))
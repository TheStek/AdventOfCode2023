with open('input.txt') as file:
	input_data = file.read()

test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

steps = ('seed-to-soil',
		'soil-to-fertilizer',
		'fertilizer-to-water',
		'water-to-light',
		'light-to-temperature',
		'temperature-to-humidity',
		'humidity-to-location')

def parse_maps(inp):
	split_maps = inp.split('\n\n')

	maps = {}

	for map_data in split_maps:
		header, data = map_data.split(':')
		if header == 'seeds':
			seeds = list(map(int, filter(lambda x: x!='', data.split(' '))))
			continue
		map_lines = list(filter(lambda x: x!= '', data.split('\n')))
		map_line_items = list(map(lambda x: list(map(int, x.split(' '))), map_lines))
		maps[header.replace(' map', '')] = map_line_items

	return seeds, maps



def map_value(mapping, value):
	for mapping_range in mapping:
		index = value - mapping_range[1]
		if index >=0 and index < mapping_range[2]:
			return mapping_range[0] + index
	return value

def seed_to_location(seed, mappings):
	
	current_value = seed
	for step in steps:
		current_value = map_value(mappings[step], current_value)
	return current_value

seeds, mappings = parse_maps(input_data)
print(min(map(lambda x: seed_to_location(x, mappings), seeds)))


seed_ranges = []

for i in range(int(len(seeds)/2)):
	seed_ranges.append([seeds[2*i], seeds[2*i+1] + seeds[2*i] - 1])

def map_range(input_range, mappings):
	debug = False
	ranges_to_map = [input_range]
	output_ranges = []
	while len(ranges_to_map) > 0:
		current_range = ranges_to_map.pop()

		for target_start, source_start, length in mappings:
			source_end = source_start + length -1

			# Completely below
			# Completely above
			if current_range[0] > source_end or current_range[1] < source_start:
				# if debug:
				# 	print('Outside', current_range, source_start, source_end)
				continue

			# Completely Within
			if current_range[0] >= source_start and current_range[1] <= source_end:
				start_index = current_range[0] - source_start
				end_index =  current_range[1] - source_start
				output_ranges.append([target_start + start_index, target_start + end_index])
				# print('Within', current_range, source_start, source_end)				
				break

			# Partially below
			if current_range[0] < source_start and current_range[1] <= source_end:
				ranges_to_map.append([current_range[0], source_start - 1])
				end_index = current_range[1] - source_start
				output_ranges.append([target_start, target_start + end_index])
				# if debug:
				# 	print('Partially below', current_range, source_start, source_end)


				break

			# Partially above
			if current_range[0] >= source_start and current_range[1] > source_end:
				ranges_to_map.append([source_end + 1, current_range[1]])
				start_index = current_range[0] - source_start
				output_ranges.append([target_start + start_index, source_end + (target_start - source_start)])
				# if debug:
				# 	print('Partially above', current_range, source_start, source_end, output_ranges[-1])

				break
		else:
			output_ranges.append(current_range)

	return output_ranges



mapped_values = {}

for i in range(len(steps)):
	if i == 0:
		current_input = seed_ranges
	else:
		current_input = mapped_values[steps[i-1]]

	mapped_values[steps[i]] = []
	for ran in current_input:
		mapped_values[steps[i]].extend(map_range(ran, mappings[steps[i]]))

print(mapped_values['humidity-to-location'])

print(min(map(lambda x: x[0], mapped_values['humidity-to-location'])))


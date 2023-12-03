with open('input.txt') as file:
	input_data = file.read().split('\n')

test_input = ['467..114..',
	'...*......',
	'..35..633.',
	'......#...',
	'617*......',
	'.....+.58.',
	'..592.....',
	'......755.',
	'...$.*....',
	'.664.598..']


def symbol_in_neighbours(r, c, schematic):
	max_row = len(schematic) - 1
	max_col = len(schematic[0]) - 1
	for check_r in range(r-1, r+2):

			if check_r < 0 or check_r > max_row:
				continue
			for check_c in range(c-1, c+2):
				if check_c < 0 or check_c > max_col:
					continue
				if (check_r, check_c) != (r, c):
					neighbour = schematic[check_r][check_c]
					if neighbour != '.' and not neighbour.isdigit():
						return True
	return False


def get_parts_in_row(row, schematic):
	parts = []
	part_start_indices = []
	pointer = 0
	max_pointer = len(schematic[row]) - 1
	current_part = None

	while pointer <= max_pointer:
		if not schematic[row][pointer].isdigit():
			if current_part:
				parts.append(current_part)
				current_part = None
			pointer += 1
			continue

		if current_part:
			current_part = current_part + schematic[row][pointer]
		else:
			current_part = schematic[row][pointer]
			part_start_indices.append(pointer)
		pointer += 1
	if current_part:
		parts.append(current_part)

	return list(zip(parts, part_start_indices))

def check_part(part_number, part_row, part_column_start, schematic):
	for i in range(len(part_number)):
		if symbol_in_neighbours(part_row, part_column_start + i, schematic):
			return True
	return False


def get_parts_in_schematic(schematic):
	parts = []
	for row in range(len(schematic)):
		candidate_parts = get_parts_in_row(row, schematic)
		for part, part_column_start in candidate_parts:
			if check_part(part, row, part_column_start, schematic):
				parts.append(part)
	return parts



print(f'Part 1: {sum(map(int, get_parts_in_schematic(input_data)))}')


def get_gear_neighbours(r, c, schematic):
		max_row = len(schematic) - 1
		max_col = len(schematic[0]) - 1
		gear_neighbours = []
		for check_r in range(r-1, r+2):

				if check_r < 0 or check_r > max_row:
					continue
				for check_c in range(c-1, c+2):
					if check_c < 0 or check_c > max_col:
						continue
					if (check_r, check_c) != (r, c):
						neighbour = schematic[check_r][check_c]
						if neighbour == '*':
							gear_neighbours.append((check_r, check_c))
		return gear_neighbours

def get_gear_neighbours_of_part(part_number, part_row, part_column_start, schematic):
	gear_neighbours = []
	for i in range(len(part_number)):
		gear_neighbours = gear_neighbours + get_gear_neighbours(part_row, part_column_start + i, schematic)

	return list(set(gear_neighbours))
	

def get_all_gear_neighbours(schematic):
	gears = {}

	for row in range(len(schematic)):
		parts = get_parts_in_row(row, schematic)
		for part_number, part_column_start in parts:
			gear_neighbours = get_gear_neighbours_of_part(part_number, row, part_column_start, schematic)
			for gear_loc in gear_neighbours:
				if gear_loc in gears.keys():
					gears[gear_loc].append(part_number)
				else:
					gears[gear_loc] = [part_number]
	return gears


def get_sum_of_gear_ratios(gears):
	total = 0
	for gear_loc, parts in gears.items():
		if len(parts) != 2:
			continue

		p1, p2 = map(int, parts)
		total += p1 * p2
	
	return total


print(f'Part 2: {get_sum_of_gear_ratios(get_all_gear_neighbours(input_data))}')
with open('input.txt', 'r') as file:
	games: list[str] = file.read().split('\n')[:-1]


test_input: list[str] = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 
	'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 
	'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 
	'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 
	'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

column_map: dict[str, int] = {'red': 0, 'green': 1, 'blue': 2}

def parse_game(game_data: str) -> list[list[int]]:

	game_matrix: list[list[int]] = []
	hands: list[str] = game_data.split('; ')
	for hand in hands:
		hand_data: list[int] = [0, 0, 0]
		dice_data: list[str] = hand.split(', ')

		for dice in dice_data:
			number, colour = dice.split(' ')
			hand_data[column_map[colour]] = int(number)
		game_matrix.append(hand_data)

	return game_matrix

def parse_games(game_input: list[str]) -> dict[int, list[list[int]]]:
	
	games_dict: dict[int, list[list[int]]] = {}

	for game in game_input:
		game_header, game_data = game.split(': ')
		game_id: int = int(game_header.split(' ')[-1])
		games_dict[game_id] = parse_game(game_data)

	return games_dict



def check_game(game_matrix: list[list[int]], totals: list[int]) -> bool:
	def check_hand(hand: list[int]) -> bool:
		for i in range(3):
			if hand[i] > totals[i]:
				return False
		return True
	for hand in game_matrix:
		if not check_hand(hand):
			return False
	return True

def get_minimum_game(game_matrix: list[list[int]]) -> list[int]:
	min_game: list[int] = [0, 0, 0]
	for hand in game_matrix:
		for i in range(3):
			if hand[i] > min_game[i]:
				min_game[i] = hand[i]

	return min_game

def multiply_list(a: list[int]) -> int:
	tot: int = 1
	for x in a:
		tot *= x
	return tot

total_possible = [12, 13, 14]

game_data_parsed = parse_games(games)

possible_ids: list[int] = []
for game_id, game_matrix in game_data_parsed.items():
	if check_game(game_matrix, total_possible):
		possible_ids.append(game_id)

print(f'Part 1: {sum(possible_ids)}')

total_power_set: int = 0
for game_matrix in game_data_parsed.values():
	min_dice: list[int] = get_minimum_game(game_matrix)
	total_power_set += multiply_list(min_dice)

print(f'Part 2: {total_power_set}')


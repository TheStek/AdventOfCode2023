from math import pow

with open('input.txt') as file:
	input_data = file.read().split('\n')[:-1]

test_input = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
	'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
	'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
	'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
	'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
	'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

def parse_card(card):
	header, data = card.split(': ')
	card_id = header.split(' ')[-1]
	winning_numbers, chosen_numbers = map(lambda x: list(filter(lambda x: x!= '', x.split(' '))), data.split(' | '))

	return (int(card_id), winning_numbers, chosen_numbers)

def get_points(card_data, part = 1):
	chosen_winning_numbers = set(card_data[2]).intersection(card_data[1])
	winning_numbers = len(chosen_winning_numbers)
	if winning_numbers == 0:
		return 0
	
	if part == 1:
		return int(pow(2, (winning_numbers - 1)))
	else:
		return winning_numbers

get_points_from_cards = lambda x: sum(map(get_points, map(parse_card, x)))

print(f'Part 1: {get_points_from_cards(input_data)}')


def process_card(card_data):
	matches = get_points(card_data, 2)
	if matches == 0:
		return

	return [original_cards[i] for i in range(card_data[0]+1, card_data[0]+1 + matches)]


cards_to_process = list(map(parse_card, input_data))
original_cards = {c[0]: c for c in cards_to_process}

current_card = 0
cache = {}  # type: ignore[var-annotated]


while current_card < len(cards_to_process):
	if cards_to_process[current_card][0] in cache.keys():
		new_cards = cache[cards_to_process[current_card][0]]
	else:
		new_cards = process_card(cards_to_process[current_card])
		cache[cards_to_process[current_card][0]] = new_cards
	if new_cards:
		cards_to_process += new_cards
	current_card += 1

print(f'Part 2: {len(cards_to_process)}')
